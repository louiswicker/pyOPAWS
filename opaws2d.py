#!/usr/bin/env python
#############################################################
# opaws2D: A program to process LVL-2 volumes, unfold       #
#          radial velocities, and thin the radar data       #
#          using a Cressman analysis scheme.                #
#          Gridded data is then written out to a DART       #
#          format file for assimilation.                    #
#                                                           #
#       Python package requirements:                        #
#       ----------------------------                        #
#       numpy                                               #
#       scipy                                               #
#       matplotlib                                          #
#       pyart (ARM-DOE python radar toolkit)                #   
#       pyproj                                              # 
#       netCDF4                                             #
#       matplotlib                                          #
#       optparse                                            #
#                                                           #
#      Originally coded by Blake Allen, August 2016         #
#############################################################
#
#        Big modifications by Lou Wicker 2016-2017
#
#############################################################
import os
import sys
import glob
import time as timeit

import numpy as np
import scipy.interpolate
import scipy.ndimage as ndimage
import scipy.spatial
from optparse import OptionParser
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredText
import netCDF4 as ncdf
import datetime as DT

from dart_tools import *
from radar_QC import *

import cressman
import pyart

from pyproj import Proj
import pylab as plt  
from mpl_toolkits.basemap import Basemap
from pyart.graph import cm


# Ignore annoying warnings (unless the code breaks, then comment these lines out)
import warnings
#warnings.filterwarnings("ignore")

# debug flag
debug = True

_thres_vr_from_ref     = True
_default_QC            = "Minimal"

# missing value
_missing = -99999.

# True here uses the basemap county database to plot the county outlines.
_plot_counties = True

# Colorscale information
_ref_scale = (0.,74.)
_vr_scale  = (-40.,40.)

# Need for Lambert conformal (default) coordinate projection
truelat1, truelat2 = 30.0, 60.0

# Parameter dict for Gridding
_grid_dict = {
              'grid_spacing_xy' : 4000.,         # meters
              'domain_radius_xy': 150000.,       # meters
              'anal_method'     : 'Cressman',    # options are Cressman, Barnes (1-pass)
              'ROI'             : 4000./0.707,   # Cressman ~ analysis_grid * sqrt(2), Barnes ~ largest data spacing in radar
              'min_count'       : 3,             # regular radar data ~3, high-res radar data ~ 10
              'min_weight'      : 0.2,           # min weight for analysis Cressman ~ 0.3, Barnes ~ 2
              'min_range'       : 10000.,        # min distance away from the radar for valid analysis (meters)
              'projection'      : 'lcc',         # map projection to use for gridded data
              'mask_vr_with_dbz': True,
              '0dbz_obtype'     : True,
              'thin_zeros'      : 4,
              'halo_footprint'  : 3,
              'nthreads'        : 1,
              'max_height'      : 10000.,
              'MRMS_zeros'      : [True,      6000.], # True: creates a single level of zeros where composite DBZ < _dbz_min
              'model_grid_size' : [750000., 750000.]  # Used to create a common grid for all observations (special option) 
             }

# Parameter dict setting radar data parameters
               
_radar_parameters = {
                     'min_dbz_analysis': 10.0, 
                     'max_range': 150000.,
                     'max_Nyquist_factor': 2,                    # dont allow output of velocities > Nyquist*factor
                     'field_label_trans': [False, "DBZC", "VR"]  # RaxPol 31 May - must specify for edit sweep files
                    }

# Dict for the standard deviation of obs_error for reflectivity or velocity (these values are squared when written to DART) 
           
_obs_errors = {
                'reflectivity'  : 5.0,
                '0reflectivity' : 5.0, 
                'velocity'      : 3.0
              }
        
#=========================================================================================
# Class variable used as container

class Gridded_Field(object):
  
  def __init__(self, name, data=None, **kwargs):    
    self.name = name    
    self.data = data    
    
    if kwargs != None:
      for key in kwargs:  setattr(self, key, kwargs[key])
      
  def keys(self):
    return self.__dict__

#=========================================================================================
# DBZ Mask

def dbz_masking(ref, thin_zeros=2):

  if _grid_dict['MRMS_zeros'][0] == True:   # create one layer of zeros based on composite ref
  
      print("\n Creating new 0DBZ levels for output\n")
      
      nz, ny, nx = ref.data.shape
      
      zero_dbz = np.ma.zeros((ny, nx), dtype=np.float32)

      c_ref = ref.data.max(axis=0)  
      
      raw_field = np.where(c_ref.mask==True, 0.0, c_ref.data)
      
      max_neighbor = (ndimage.maximum_filter(raw_field, size=_grid_dict['halo_footprint']) > 0.1)
      
      zero_dbz.mask = np.where(max_neighbor, True, False)

# the trick here was to realize that you need to first flip the zero_dbz_mask array and then thin by shutting off mask      
      if thin_zeros > 0:
          mask2 = np.logical_not(zero_dbz.mask)                                            # true for dbz>10
          mask2[::thin_zeros, ::thin_zeros] = False
          zero_dbz.mask = np.logical_or(max_neighbor, mask2)
      
      ref.zero_dbz = zero_dbz

      new_z = np.ma.zeros((2, ny, nx), dtype=np.float32)

      for n, z in enumerate(_grid_dict['MRMS_zeros'][1:]):
          new_z[n] = z
                
      ref.zero_dbz_zg = new_z
      ref.cref        = c_ref
     
  else: 
      mask = (ref.data.mask == True)  # this is the original no data mask from interp
  
      ref.data.mask = False           # set the ref mask to false everywhere
    
      ref.data[mask] = 0.0             
  
      nlevel = ref.data.shape[0]
  
      for n in np.arange(nlevel):  
          max_values = ndimage.maximum_filter(ref.data[n,:,:], size=_grid_dict['halo_footprint'])
          halo  = (max_values > 0.1) & mask[n]    
          ref.data.mask[n,halo] = True

      if thin_zeros > 0:

          for n in np.arange(nlevel):   
              mask1 = np.logical_and(ref.data[n] < 0.1, ref.data.mask[n] == False)  # true for dbz=0
              mask2 = ref.data.mask[n]                                              # true for dbz>10
              mask1[::thin_zeros, ::thin_zeros] = False
              ref.data.mask[n] = np.logical_or(mask1, mask2)

  if _grid_dict['max_height'] > 0:
      mask1  = (ref.zg - ref.radar_hgt) > _grid_dict['max_height']
      mask2 = ref.data.mask
      ref.data.mask = np.logical_or(mask1, mask2)
        
  return ref

#=========================================================================================
# VR Masking

def vel_masking(vel, ref, volume):

# Mask the radial velocity where dbz is masked

   print "Size of input VR  mask ", np.sum(vel.data.mask)
   print "Size of input dBZ mask ", np.sum(ref.data.mask)

   vel.data.mask = np.logical_or(vel.data.mask, ref.data.mask)

# Limit max/min values of radial velocity (bad unfolding, too much "truth")

#  Commented out because of high velocities in hurricanes

#  for m in np.arange(volume.nsweeps):
#      Vr_max = volume.get_nyquist_vel(m)
#      mask1  = (np.abs(vel.data[m]) > _radar_parameters['max_Nyquist_factor']*Vr_max)                 
#      vel.data.mask[m] = np.logical_or(vel.data.mask[m], mask1)
        
   if _grid_dict['max_height'] > 0:
      mask1 = (vel.zg - vel.radar_hgt) > _grid_dict['max_height']
      print "Size of height mask: ", np.sum(mask1)
      mask2 = vel.data.mask
      print "Size of VR + dBZ mask: ", np.sum(mask2)
      vel.data.mask = np.logical_or(mask1, mask2)
      print "Size of new mask ", np.sum(vel.data.mask)
      
   return vel
      
########################################################################
#
# Grid data using parameters defined above in grid_dict 

def grid_data(volume, field, LatLon=None):
 
# Two ways to grid the data:  radar centered or external grid
 
   if LatLon == None:   # the grid is centered on the radar
   
       grid_spacing_xy = _grid_dict['grid_spacing_xy']
       domain_length   = _grid_dict['domain_radius_xy']
       grid_pts_xy     = 1 + 2*np.int(domain_length/grid_spacing_xy)
       nx, ny          = (grid_pts_xy, grid_pts_xy)
       radar_lat       = volume.latitude['data'][0]
       radar_lon       = volume.longitude['data'][0]
       xg              = -domain_length + grid_spacing_xy * np.arange(grid_pts_xy)
       yg              = -domain_length + grid_spacing_xy * np.arange(grid_pts_xy)
       
       map = Proj(proj='lcc', ellps='WGS84', datum='WGS84', lat_1=truelat1, lat_2=truelat2, lat_0=radar_lat, lon_0=radar_lon)
       xoffset, yoffset = map(radar_lon, radar_lat) 
       lons, lats = map(xg, yg, inverse=True)
      
   else:  # grid based on model grid center LatLon
   
       grid_spacing_xy = _grid_dict['grid_spacing_xy']
       nx              = 1 + np.int(_grid_dict['model_grid_size'][0] / grid_spacing_xy)
       ny              = 1 + np.int(_grid_dict['model_grid_size'][1] / grid_spacing_xy)
       grid_pts_xy     = max(nx, ny)
       xg              = -0.5*_grid_dict['model_grid_size'][0] + grid_spacing_xy * np.arange(nx)
       yg              = -0.5*_grid_dict['model_grid_size'][1] + grid_spacing_xy * np.arange(ny)
       radar_lat       = volume.latitude['data'][0]
       radar_lon       = volume.longitude['data'][0]
       
       map = Proj(proj='lcc', ellps='WGS84', datum='WGS84', lat_1=truelat1, lat_2=truelat2, lat_0=LatLon[0], lon_0=LatLon[1])
        
       xoffset, yoffset = map(radar_lon, radar_lat)
       lons, lats = map(xg, yg, inverse=True)

   if _grid_dict['anal_method'] == 'Cressman':
      anal_method = 1
   else:
      anal_method = 2

   roi        = _grid_dict['ROI']
   nthreads   = _grid_dict['nthreads']
   min_count  = _grid_dict['min_count']
   min_weight = _grid_dict['min_weight']
   min_range  = _grid_dict['min_range']

########################################################################
  
   print '\n Gridding radar data with following parameters'
   print ' ---------------------------------------------\n'
   print ' Method of Analysis:      {}'.format(_grid_dict['anal_method'])
   print ' Horizontal grid spacing: {} km'.format(grid_spacing_xy/1000.)
   print ' Grid points in x,y:      {},{}'.format(int(nx),int(ny))
   print ' Weighting function:      {}'.format(_grid_dict['anal_method'])
   print ' Radius of Influence:     {} km'.format(_grid_dict['ROI']/1000.)
   print ' Minimum gates:           {}'.format(min_count)
   print ' Minimum weight:          {}'.format(min_weight)
   print ' Minimum range:           {} km'.format(min_range/1000.)
   print ' Map projection:          {}'.format(_grid_dict['projection'])
   print ' Xoffset:                 {} km'.format(np.round(xoffset/1000.))
   print ' Yoffset:                 {} km'.format(np.round(yoffset/1000.))
   print ' Field to be gridded:     {}\n'.format(field) 
   print ' Min / Max X grid loc:    {} <-> {} km\n'.format(0.001*xg[0], 0.001*xg[-1])
   print ' Min / Max Y grid loc:    {} <-> {} km\n'.format(0.001*yg[0], 0.001*yg[-1])
   print ' Min / Max Longitude:     {} <-> {} deg\n'.format(lons[0], lons[-1])
   print ' Min / Max Latitude:      {} <-> {} deg\n'.format(lats[0], lats[-1])
   print ' ---------------------------------------------\n' 

########################################################################
#
# Local weight function for pyresample

   def wf(z_in):
    
       if _grid_dict['anal_method'] == 'Cressman':
           w    = np.zeros((z_in.shape), dtype=np.float64)
           ww   = (roi**2 - z_in**2) / (roi**2 + z_in**2)
           mask = (np.abs(z_in) <  roi)
           w[mask] = ww[mask] 
           return w
          
       elif _grid_dict['anal_method'] == 'test':
           return np.ones((z_in.shape), dtype=np.float64)
          
       elif _grid_dict['anal_method'] == 'Barnes':

           return np.exp(-(z_in/roi)**2)
          
       else:  # Gasparoi and Cohen...

           gc = np.zeros((z_in.shape), dtype=np.float64)
           z = abs(z_in)
           r = z / roi
           z1 = (((( r/12.  -0.5 )*r  +0.625 )*r +5./3. )*r  -5. )*r + 4. - 2./(3.*r)
           z2 = ( ( ( -0.25*r +0.5 )*r +0.625 )*r  -5./3. )*r**2 + 1.
           m1 = np.logical_and(z >= roi, z < 2*roi)
           m2 = (z <  roi)
           gc[m1] = z1[m1]
           gc[m2] = z2[m2]      
           return gc


   tt = timeit.clock()

#####################################################################################   
   try:
       v_iter = volume.iter_field(field)
       field_name = field
   except KeyError:
       print("\n No dealiased velocity present, gridding RAW radial velocity\n")
       v_iter = volume.iter_field("velocity")
       field_name = "velocity"
       
   if field == "reflectivity":
       sweeps = volume.reflectivity
   else:
       sweeps = volume.velocity

#####################################################################################
# Create 3D arrays for analysis grid, the vertical dimension is the number of tilts

   new         = np.ma.zeros((len(sweeps), ny, nx))
   elevations  = np.zeros((len(sweeps),))
   sweep_time  = np.zeros((len(sweeps),))
   zgrid       = np.zeros((len(sweeps), ny, nx))
   nyquist     = np.zeros((len(sweeps),))
       
# Grid only those valid sweeps 
  
   for n, sweep_level in enumerate(sweeps):
   
       sweep_data = volume.get_field(sweep_level, field_name)

       begin, end = volume.get_start_end(sweep_level)
      
       sweep_time[n] = volume.time['data'][begin:end].mean()
       elevations[n] = volume.get_elevation(sweep_level).mean()
       nyquist[n]    = volume.get_nyquist_vel(sweep_level)
       
       omask = (sweep_data.mask == False)
       
       x, y, z = volume.get_gate_x_y_z(sweep_level)
    
       obs = sweep_data[omask].ravel()
       xob = x[omask].ravel() + xoffset
       yob = y[omask].ravel() + yoffset
       
       ix = np.searchsorted(xg, xob)
       iy = np.searchsorted(yg, yob)
    
       if obs.size > 0:
           tmp = cressman.obs_2_grid2d(obs, xob, yob, xg, yg, ix, iy, anal_method, min_count, min_weight, min_range, \
                                       2.0*grid_spacing_xy, _missing)
           new_mask = (tmp <= _missing)
           new[n] = np.ma.array(tmp, mask=new_mask)
       else:
           new[n] = np.ma.masked_all((grid_pts_xy, grid_pts_xy))
        
       print(" Sweep: %2.2d Elevation: %5.2f  Number of valid grid points:  %d" % (n, elevations[n],np.sum(new[n].mask==False)))

       if field == "reflectivity":
           new[n].mask = np.logical_or(new[n].mask, new[n] < _radar_parameters['min_dbz_analysis'])
           print(" Sweep: %2.2d Elevation: %5.2f  Number of valid reflectivity points:  %d" % \
                        (n, elevations[n],np.sum(new[n].mask==False)))

   # Create z-field

       zobs= z.ravel()
       xob = x.ravel() + xoffset
       yob = y.ravel() + yoffset

       zobs = np.where( zobs < 0.0, 0.0, zobs)
    
       ix = np.searchsorted(xg, xob)
       iy = np.searchsorted(yg, yob)

#      tmp=inverse_distance(xob, yob, zobs, xg, yg, 2.0*grid_spacing_xy, gamma=None, kappa=None,
#                    min_neighbors=min_count, kind='cressman')

       tmp = cressman.obs_2_grid2d(zobs, xob, yob, xg, yg, ix, iy, 1, 1, 0.1, min_range, 2.0*grid_spacing_xy, -99999.)
       new_mask = (tmp == -99999.)
       zgrid[n] = np.ma.array(tmp, mask=new_mask)
    
   print("\n %f secs to run superob analysis for all levels \n" % (timeit.clock()-tt))

   return Gridded_Field("data_grid", field = field, data = new, basemap = map, 
                        xg = xg, yg = yg, zg = zgrid,                   
                        lats = lats, lons = lons, elevations=elevations,
                        radar_lat = radar_lat, radar_lon = radar_lon, radar_hgt=volume.altitude['data'][0],
                        time = volume.time, sweep_time = sweep_time, metadata = volume.metadata, nyquist = nyquist  ) 

###########################################################################################
#
# Read environment variables for plotting a shapefile

def plot_shapefiles(map, shapefiles=None, color='k', linewidth=0.5, counties=False, ax=None):

    if shapefiles:
        try:
            shapelist = os.getenv(shapefiles).split(":")

            if len(shapelist) > 0:

                for item in shapelist:
                    items      = item.split(",")
                    shapefile  = items[0]
                    color      = items[1]
                    linewidth  = items[2]

                    s = map.readshapefile(shapefile,'myshapes',drawbounds=False)

                    for shape in map.counties:
                        xx, yy = zip(*shape)
                        map.plot(xx, yy, color=color, linewidth=linewidth, ax=ax, zorder=4)

        except OSError:
            print "PLOT_SHAPEFILES:  NO SHAPEFILE ENV VARIABLE FOUND "
            
    if counties:
            map.drawcounties(ax=ax, linewidth=0.5, color='k', zorder=5)
            
########################################################################
#
# Create two panel plot of processed, gridded velocity and reflectivity data  

def plot_gridded(ref, vel, sweep, fsuffix=None, dir=".", shapefiles=None, interactive=True, LatLon=None):
  
# Set up colormaps 

  from matplotlib.colors import BoundaryNorm
   
  cmapr = cm.NWSRef
  cmapr.set_bad('white',1.0)
  cmapr.set_under('white',1.0)

  cmapv = cm.Carbone42
  cmapv.set_bad('white',1.)
  cmapv.set_under('black',1.)
  cmapv.set_over('black',1.)
  
  normr = BoundaryNorm(np.arange(10, 85, 5), cmapr.N)
  normv = BoundaryNorm(np.arange(-48, 50, 2), cmapv.N)
  
  min_dbz = _radar_parameters['min_dbz_analysis']  
  xwidth = ref.xg.max() - ref.xg.min()
  ywidth = ref.yg.max() - ref.yg.min()

# Create png file label

  if fsuffix == None:
      print("\n opaws2D.grid_plot:  No output file name is given, writing to %s" % "VR_RF_...png")
      filename = "%s/VR_RF_%2.2d_plot.pdf" % (dir, sweep)
  else:
       filename = "%s/VR_RF_%2.2d_%s.pdf" % (dir, sweep, fsuffix.split("/")[1])

  fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(25,14))
  
# Set up coordinates for the plots

  if LatLon == None:
      bgmap = Basemap(projection=_grid_dict['projection'], width=xwidth, \
                  height=ywidth, resolution='c', lat_0=ref.radar_lat, lon_0=ref.radar_lon, ax=ax1)
      xoffset, yoffset = bgmap(ref.radar_lon, ref.radar_lat)
      xg, yg = bgmap(ref.lons, ref.lats)
  else:
      bgmap = Basemap(projection=_grid_dict['projection'], width=xwidth, \
                  height=ywidth, resolution='c', lat_0=LatLon[0], lon_0=LatLon[1], ax=ax1)
      xoffset, yoffset = bgmap(ref.radar_lon, ref.radar_lat)    
      xg, yg = bgmap(ref.lons, ref.lats)
      
#   print xg.min(), xg.max(), xg.shape
#   print yg.min(), yg.max(), yg.shape
  
  xg_2d, yg_2d = np.meshgrid(xg, yg)
 
#   print xg.min(), xg_2d[0,0], xg_2d[-1,-1], xg.max(), xg.shape
#   print yg.min(), yg.max(), yg.shape
 
# fix xg, yg coordinates so that pcolormesh plots them in the center.

  dx2 = 0.5*(ref.xg[1] - ref.xg[0])
  dy2 = 0.5*(ref.yg[1] - ref.yg[0])
  
  xe = np.append(xg-dx2, [xg[-1] + dx2])
  ye = np.append(yg-dy2, [yg[-1] + dy2])

# REFLECTVITY PLOT

  if shapefiles:
      plot_shapefiles(bgmap, shapefiles=shapefiles, counties=_plot_counties, ax=ax1)
  else:
      plot_shapefiles(bgmap, counties=_plot_counties, ax=ax1)
 
  bgmap.drawparallels(range(10,80,1),    labels=[1,0,0,0], linewidth=0.5, ax=ax1)
  bgmap.drawmeridians(range(-170,-10,1), labels=[0,0,0,1], linewidth=0.5, ax=ax1)

  im1 = bgmap.pcolormesh(xe, ye, ref.data[sweep], cmap=cmapr, vmin = _ref_scale[0], vmax = _ref_scale[1], ax=ax1)
  cbar = bgmap.colorbar(im1, location='right')
  cbar.set_label('Reflectivity (dBZ)')
  ax1.set_title('Thresholded Reflectivity (Gridded)')
  bgmap.scatter(xoffset,yoffset, c='k', s=50., alpha=0.8, ax=ax1)
  
  at = AnchoredText("Max dBZ: %4.1f" % (ref.data[sweep].max()), loc=4, prop=dict(size=12), frameon=True,)
  at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
  ax1.add_artist(at)

# Plot zeros as "o"

  try:
      r_mask = (ref.zero_dbz.mask == False)
      print("\n Plotting zeros from MRMS level\n")
      bgmap.scatter(xg_2d[r_mask], yg_2d[r_mask], s=25, facecolors='none', \
                    edgecolors='k', alpha=1.0, ax=ax1) 
                    
  except AttributeError:
      print("\n Plotting zeros from full 3D grid level (non-MRMS form)\n")
      r_mask = np.logical_and(ref.data[sweep] < 1.0, (ref.data.mask[sweep] == False))
      bgmap.scatter(xg_2d[r_mask], yg_2d[r_mask], s=25, facecolors='none', \
                    edgecolors='k', alpha=1.0, ax=ax1)
  
# RADIAL VELOCITY PLOT

  if LatLon == None:
      bgmap = Basemap(projection=_grid_dict['projection'], width=xwidth, \
                  height=ywidth, resolution='c', lat_0=ref.radar_lat,lon_0=ref.radar_lon, ax=ax2)
      xoffset, yoffset = bgmap(ref.radar_lon, ref.radar_lat)
  else:
      bgmap = Basemap(projection=_grid_dict['projection'], width=xwidth, \
                  height=ywidth, resolution='c', lat_0=LatLon[0], lon_0=LatLon[1], ax=ax2)
      xoffset, yoffset = bgmap(ref.radar_lon, ref.radar_lat)            
  
                  
  if shapefiles:
      plot_shapefiles(bgmap, shapefiles=shapefiles, counties=_plot_counties, ax=ax2)
  else:
      plot_shapefiles(bgmap, counties=_plot_counties, ax=ax2)
    
  bgmap.drawparallels(range(10,80,1),labels=[1,0,0,0], linewidth=0.5, ax=ax2)
  bgmap.drawmeridians(range(-170,-10,1),labels=[0,0,0,1],linewidth=0.5, ax=ax2)
  
  im1 = bgmap.pcolormesh(xe, ye, vel.data[sweep], cmap=cmapv, vmin=_vr_scale[0], vmax=_vr_scale[1], ax=ax2)
  cbar = bgmap.colorbar(im1,location='right')
  cbar.set_label('Dealised Radial Velocity (meters_per_second)')
  ax2.set_title('Thresholded, Unfolded Radial Velocity (Gridded)') 
  bgmap.scatter(xoffset,yoffset, c='k', s=50., alpha=0.8, ax=ax2)

  at = AnchoredText("Max Vr: %4.1f \nMin Vr: %4.1f " % \
                 (vel.data[sweep].max(),vel.data[sweep].min()), loc=4, prop=dict(size=12), frameon=True,)
  at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
  ax2.add_artist(at)  
    
# Now plot locations of nan data

  v_mask = (vel.data.mask == True)
  bgmap.scatter(xg_2d[v_mask[sweep]], yg_2d[v_mask[sweep]], c='k', s = 1., alpha=0.5, ax=ax2)

# Get other metadata....for labeling

  instrument_name = ref.metadata['instrument_name']
  time_start = ncdf.num2date(ref.time['data'][0], ref.time['units'])
  time_text = time_start.isoformat().replace("T"," ")
  title = '\nDate:  %s   Time:  %s Z   Elevation:  %2.2f deg' % (time_text[0:10], time_text[10:19], ref.elevations[sweep])
  plt.suptitle(title, fontsize=24)
  
  plt.savefig(filename)
  
  if interactive:  plt.show()

#####################################################################################################
def write_radar_file(ref, vel, filename=None):
    
  _time_units    = 'seconds since 1970-01-01 00:00:00'
  _calendar      = 'standard'

  if filename == None:
      print("\n write_DART_ascii:  No output file name is given, writing to %s" % "obs_seq.txt")
      filename = "obs_seq.nc"
  else:
      dirname = os.path.dirname(filename)
      basename = "%s_%s.nc" % ("obs_seq", os.path.basename(filename))
      filename =  os.path.join(dirname, basename)

  _stringlen     = 8
  _datelen       = 19
     
# Extract grid and ref data
        
  dbz        = ref.data
  lats       = ref.lats
  lons       = ref.lons
  hgts       = ref.zg + ref.radar_hgt
  kind       = ObType_LookUp(ref.field.upper())  
  R_xy       = np.sqrt(ref.xg[20]**2 + ref.yg[20]**2)
  elevations = beam_elv(R_xy, ref.zg[:,20,20])
  
# if there is a zero dbz obs type, reform the data array 
  try:
      nx1, ny1       = ref.zero_dbz.shape
      zero_data      = np.ma.zeros((2, ny1, nx1), dtype=np.float32)
      zero_hgts      = np.ma.zeros((2, ny1, nx1), dtype=np.float32)
      zero_data[0]   = ref.zero_dbz
      zero_data[1]   = ref.zero_dbz
      zero_hgts[0:2] = ref.zero_dbz_zg[0:2]
      cref           = ref.cref
      zero_flag = True
      print("\n write_DART_ascii:  0-DBZ separate type added to netcdf output\n")
  except AttributeError:
      zero_flag = False
      print("\n write_DART_ascii:  No 0-DBZ separate type found\n")
      
# Extract velocity data
  
  vr                  = vel.data
  platform_lat        = vel.radar_lat
  platform_lon        = vel.radar_lon
  platform_hgt        = vel.radar_hgt

# Use the volume mean time for the time of the volume
      
  dtime   = ncdf.num2date(ref.time['data'].mean(), ref.time['units'])
  days    = ncdf.date2num(dtime, units = "days since 1601-01-01 00:00:00")
  seconds = np.int(86400.*(days - np.floor(days)))  
  
# create the fileput filename and create new netCDF4 file

#filename = os.path.join(path, "%s_%s%s" % ("Inflation", DT.strftime("%Y-%m-%d_%H:%M:%S"), ".nc" ))

  print "\n -->  Writing %s as the radar file..." % (filename)
    
  rootgroup = ncdf.Dataset(filename, 'w', format='NETCDF4')
      
# Create dimensions

  shape = dbz.shape
  
  rootgroup.createDimension('nz',   shape[0])
  rootgroup.createDimension('ny',   shape[1])
  rootgroup.createDimension('nx',   shape[2])
  rootgroup.createDimension('stringlen', _stringlen)
  rootgroup.createDimension('datelen', _datelen)
  if zero_flag:
      rootgroup.createDimension('nz2',   2)
  
# Write some attributes

  rootgroup.time_units   = _time_units
  rootgroup.calendar     = _calendar
  rootgroup.stringlen    = "%d" % (_stringlen)
  rootgroup.datelen      = "%d" % (_datelen)
  rootgroup.platform_lat = platform_lat
  rootgroup.platform_lon = platform_lon
  rootgroup.platform_hgt = platform_hgt

# Create variables

  R_type  = rootgroup.createVariable('REF', 'f4', ('nz', 'ny', 'nx'), zlib=True, shuffle=True )    
  V_type  = rootgroup.createVariable('VEL', 'f4', ('nz', 'ny', 'nx'), zlib=True, shuffle=True )
  
  if zero_flag:
      R0_type   = rootgroup.createVariable('0REF',  'f4', ('nz2', 'ny', 'nx'), zlib=True, shuffle=True )    
      Z0_type   = rootgroup.createVariable('0HGTS', 'f4', ('nz2', 'ny', 'nx'), zlib=True, shuffle=True )
      CREF_type = rootgroup.createVariable('CREF', 'f4', ('ny', 'nx'), zlib=True, shuffle=True )
      
  V_dates = rootgroup.createVariable('date', 'S1', ('datelen'), zlib=True, shuffle=True)
  V_xc    = rootgroup.createVariable('XC', 'f4', ('nx'), zlib=True, shuffle=True)
  V_yc    = rootgroup.createVariable('YC', 'f4', ('ny'), zlib=True, shuffle=True)
  V_el    = rootgroup.createVariable('EL', 'f4', ('nz'), zlib=True, shuffle=True)

  V_lat   = rootgroup.createVariable('LATS', 'f4', ('ny'), zlib=True, shuffle=True)
  V_lon   = rootgroup.createVariable('LONS', 'f4', ('nx'), zlib=True, shuffle=True)
  V_hgt   = rootgroup.createVariable('HGTS', 'f4', ('nz', 'ny', 'nx'), zlib=True, shuffle=True)

# Write variables

  rootgroup.variables['date'][:] = ncdf.stringtoarr(dtime.strftime("%Y-%m-%d_%H:%M:%S"), _datelen)
  
  rootgroup.variables['REF'][:]  = dbz[:]
  rootgroup.variables['VEL'][:]  = vr[:]
  rootgroup.variables['XC'][:]   = ref.xg[:]
  rootgroup.variables['YC'][:]   = ref.yg[:]
  rootgroup.variables['EL'][:]   = elevations[:]
  rootgroup.variables['HGTS'][:] = ref.zg[:]
  rootgroup.variables['LATS'][:] = lats[:]
  rootgroup.variables['LONS'][:] = lons[:]
  
  if zero_flag:
       rootgroup.variables['0REF'][:]   = zero_data
       rootgroup.variables['0HGTS'][:]  = zero_hgts
       rootgroup.variables['CREF'][:]   = cref
  
  rootgroup.sync()
  rootgroup.close()
  
  return filename  
  
########################################################################
# Main function

if __name__ == "__main__":

   print ' ================================================================================'
   print ''
   print '                   BEGIN PROGRAM opaws2D                     '
   print ''

   parser = OptionParser()
   
   parser.add_option("-d", "--dir",       dest="dname",     default=None,  type="string", \
           help = "Directory of files to process")
                     
   parser.add_option("-o", "--out",       dest="out_dir",     default="opaws_files",  type="string", \
           help = "Directory to place output files in")
                     
   parser.add_option("-f", "--file",      dest="fname",     default=None,  type="string", \
           help = "filename of NEXRAD level II volume or cfradial file to process")
                     
   parser.add_option("-u", "--unfold",    dest="unfold",    default="region",  type="string", \
           help = "dealiasing method to use (phase or region, default = phase)")
                     
   parser.add_option("-w", "--write",     dest="write",   default=False, \
           help = "Boolean flag to write DART ascii file", action="store_true")
                     
   parser.add_option(     "--method",     dest="method",   default=None, type="string", \
           help = "Function to use for the weight process, valid strings are:  Cressman or Barnes")
          
   parser.add_option("-q", "--qc", dest="qc", default="Minimal",  type="string",     \
           help = "Type of QC corrections on reflectivity or velocity.  Valid:  None, Minimal, MetSignal, A1")  

   parser.add_option(     "--dx",     dest="dx",   default=None, type="float", \
           help = "Analysis grid spacing in meters for superob resolution")
          
   parser.add_option(     "--roi",     dest="roi",   default=None, type="float", \
           help = "Radius of influence in meters for superob regrid")

   parser.add_option("-p", "--plot",      dest="plot",      default=-1,  type="int",      \
           help = "Specify a number between 0 and # elevations to plot ref and vr in that co-plane")
                     
   parser.add_option("-i", "--interactive", dest="interactive", default=False,  action="store_true",     \
           help = "Boolean flag to specify to plot image to screen (when plot > -1).")  
                     
   parser.add_option("-s", "--shapefiles", dest="shapefiles", default=None, type="string",    \
           help = "Name of system env shapefile you want to add to the plots.")
                     
   parser.add_option(      "--newse",    dest="newse",    type="string", default=None, \
           help = "NEWSe radars description file to parse for model grid lat and lon" )

   (options, args) = parser.parse_args()
  
   parser.print_help()

   print ''
   print ' ================================================================================'

# Create directory for output files
  
   if not os.path.exists(options.out_dir):
       os.mkdir(options.out_dir)

   out_filenames = []
   in_filenames  = []

   if options.dname == None:
          
       if options.fname == None:
           print "\n\n ***** USER MUST SPECIFY NEXRAD LEVEL II (MESSAGE 31) FILE! *****"
           print "\n\n *****                     OR                               *****"
           print "\n\n *****               CFRADIAL FILE!                         *****"
           print "\n                         EXITING!\n\n"
           parser.print_help()
           print
           sys.exit(1)
      
       else:
           in_filenames.append(os.path.abspath(options.fname))
           strng = os.path.basename(in_filenames[0]).split("_V06")[0]
           strng = strng[0:4] + "_" + strng[4:]
           strng = os.path.join(options.out_dir, strng)
           out_filenames.append(strng) 

   else:
       in_filenames = glob.glob("%s/*" % os.path.abspath(options.dname))
       print("\n opaws2D:  Processing %d files in the directory:  %s\n" % (len(in_filenames), options.dname))
       print("\n opaws2D:  First file is %s\n" % (in_filenames[0]))
       print("\n opaws2D:  Last  file is %s\n" % (in_filenames[-1]))
       print("\n opaws2D:  Last  file is %s\n" % (in_filenames[0][-3:]))
 
       if in_filenames[0][-3:] == "V06" or in_filenames[0][-6:] == "V06.gz":
           for item in in_filenames:
               strng = os.path.basename(item).split("_V06")[0]
               strng = strng[0:4] + "_" + strng[4:]
               strng = os.path.join(options.out_dir, strng)
               out_filenames.append(strng) 
               print(strng)
        
       if in_filenames[0][-3:] == ".nc":
           for item in in_filenames:
               strng = os.path.basename(item).split(".")[0:2]
               print strng
               strng = strng[0] + "_" + strng[1]
               strng = os.path.join(options.out_dir, strng)
               out_filenames.append(strng) 
               print strng

   if options.unfold == "phase":
       print "\n opaws2D dealias_unwrap_phase unfolding will be used\n"
       unfold_type = "phase"
   elif options.unfold == "region":
       print "\n opaws2D dealias_region_based unfolding will be used\n"
       unfold_type = "region"
   else:
       print "\n ***** INVALID OR NO VELOCITY DEALIASING METHOD SPECIFIED *****"
       print "\n          NO VELOCITY UNFOLDING DONE...\n\n"
       unfold_type = None

   if options.newse:
       print(" \n now processing NEWSe radar file....\n ")
       cLatLon = parse_NEWSe_radar_file(options.newse, getLatLon=True)
   else:
       cLatLon = None
    
   if options.method:
        _grid_dict['anal_method'] = options.method

   if options.dx:
        _grid_dict['grid_spacing_xy'] = options.dx
        _grid_dict['ROI'] = options.dx / 0.707
       
   if options.roi:
      _grid_dict['ROI'] = options.roi

   if options.plot < 0:
       plot_grid = False
   else:
       sweep_num = options.plot
       plot_grid = True
       if not os.path.exists("images"):
           os.mkdir("images")

# Read input file and create radar object

   t0 = timeit.time()

   for n, fname in enumerate(in_filenames):

       print '\n Reading: {}\n'.format(fname)
       print '\n Writing: {}\n'.format(out_filenames[n])
   
       tim0 = timeit.time()

 # the check for file size is to make sure there is data in the LVL2 file
       try:
           if os.path.getsize(fname) < 2048000:
               print '\n File {} is less than 2 mb, skipping...\n'.format(fname)
               continue
       except:
           continue
      
       if fname[-3:] == ".nc":
         if _radar_parameters['field_label_trans'][0] == True:
             REF_LABEL = _radar_parameters['field_label_trans'][1]
             VEL_LABEL = _radar_parameters['field_label_trans'][2]
             volume = pyart.io.read_cfradial(fname, field_names={REF_LABEL:"reflectivity", VEL_LABEL:"velocity"})
         else:
             volume = pyart.io.read_cfradial(fname)
       else:
         try:
           volume = pyart.io.read_nexrad_archive(fname, field_names=None, 
                                                 additional_metadata=None, file_field_names=False, 
                                                 delay_field_loading=False, 
                                                 station=None, scans=None, linear_interp=True)
         except:
           print '\n File {} cannot be read, skipping...\n'.format(fname)
           continue

       opaws2D_io_cpu = timeit.time() - tim0
  
       print "\n Time for reading in LVL2: {} seconds".format(opaws2D_io_cpu)

# Modern level-II files need to be mapped to figure out where the super-res velocity and reflectivity fields are located in file
 
       ret = volume_mapping(volume)
       
# For some reason, you need to do velocity unfolding first....then QC the rest of the data

       tim0 = timeit.time()      

       print '\n ================================================================================'

       if unfold_type == None:
           vr_field = "velocity"
           vr_label = "Radial Velocity"
       else:
           try:
               print("\n Trying %s-based unfolding method\n" % unfold_type)
               ret = velocity_unfold(volume, unfold_type=unfold_type, gatefilter=None) 
               vr_field = "unfolded velocity"
               vr_label = "Unfolded Radial Velocity"
           except:
               print("\n ----> %s unfolding method has failed!! Trying alternate unfolding method\n" % unfold_type)
               try:
                   unfold_type2 = "region"
                   if unfold_type == "region":    
                       unfold_type2 = "phase"
                   ret = velocity_unfold(volume, unfold_type=unfold_type2, gatefilter=None) 
                   vr_field = "unfolded velocity"
                   vr_label = "Unfolded Radial Velocity"
               except:
                   print("\n ----> Both unfolding methods have failed!! Turning off unfolding\n\n")
                   vr_field = "velocity"
                   vr_label = "Radial Velocity"

       opaws2D_unfold_cpu = timeit.time() - tim0

       print "\n Time for unfolding velocity: {} seconds".format(opaws2D_unfold_cpu)

       print '\n ================================================================================'
  
# Now we do QC

       tim0 = timeit.time()

       if options.qc == "None":
           print("\n No quality control will be done on data\n")
           gatefilter = volume_prep(volume, QC_type = options.qc, thres_vr_from_ref = False, \
                                    max_range = _radar_parameters['max_range'])
       else:
           print("\n QC type:  %s \n" % options.qc)
           gatefilter = volume_prep(volume, QC_type = options.qc, thres_vr_from_ref = _thres_vr_from_ref, \
                                    max_range = _radar_parameters['max_range'])


       opaws2D_QC_cpu = timeit.time() - tim0
       
       print "\n Time for quality controling the data: {} seconds".format(opaws2D_QC_cpu)
       print '\n ================================================================================'

       tim0 = timeit.time()
       
# Now grid the reflectivity (embedded call) and then mask it off based on parameters set at top

       ref = dbz_masking(grid_data(volume, "reflectivity", LatLon=cLatLon), thin_zeros=_grid_dict['thin_zeros'])

# Finally, regrid the radial velocity
 
       if unfold_type == None:  
           vel = grid_data(volume, "velocity", LatLon=cLatLon)
       
       else:
           vel = grid_data(volume, "unfolded velocity", LatLon=cLatLon)

# Mask it off based on dictionary parameters set at top

       if _grid_dict['mask_vr_with_dbz']:
           vel = vel_masking(vel, ref, volume)
    
       opaws2D_regrid_cpu = timeit.time() - tim0
  
       print "\n Time for gridding fields: {} seconds".format(opaws2D_regrid_cpu)
       
       print '\n ================================================================================'

       if plot_grid:
           fplotname = out_filenames[n]
           plottime = plot_gridded(ref, vel, sweep_num, fsuffix=fplotname, dir=options.out_dir, \
                      shapefiles=options.shapefiles, interactive=options.interactive, LatLon=cLatLon)

       if options.write == True:      
           ret = write_DART_ascii(vel, filename=out_filenames[n]+"_VR", grid_dict=_grid_dict, \
                                  obs_error=[_obs_errors['velocity']] )
           ret = write_DART_ascii(ref, filename=out_filenames[n]+"_RF", grid_dict=_grid_dict, \
                                  obs_error=[_obs_errors['reflectivity'], _obs_errors['0reflectivity']])
           
           ret = write_radar_file(ref, vel, filename=out_filenames[n])
  
   opaws2D_cpu_time = timeit.time() - t0

   print "\n Time for opaws2D operations: {} seconds".format(opaws2D_cpu_time)

   print "\n PROGRAM opaws2D COMPLETED\n"
