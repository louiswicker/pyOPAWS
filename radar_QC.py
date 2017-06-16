####

import sys
import numpy as np
import scipy.interpolate
import scipy.ndimage as ndimage
import scipy.spatial
import pyart

_met_signal_mask_value = {"reflectivity": 70., "velocity": 50.}

# Values from Krause (2016) for metsignal values

_min_dbz               = 10.
_spw_filter            = 5.0
_rhv_filter            = 0.90
_zdr_filter            = 2.0

# This turns debugging info

_verbose_QC = False

########################################################################
# Volume mapping

def volume_mapping(radar):

# Dealing with split cuts is a pain in the ass....create a lookup table to connect sweeps
# Weird thing:  there IS reflectivity on all the VR sweeps, but no dual-pol data.  
# I have decided to use the reflectivity field associated with the VR scan to be used for the
# masking, but if MetSignal QC is called, the next lowest tilt will be used to compute the
# met-signal mask, since the algorithm requires the dual-pol data.

# Store this information in a hash tables added tp pyart radar object....

   radar.sweep_table = []
   radar.reflectivity = []
   radar.velocity = []

# Create a list of elevations
   
   elist = [x.shape[0] for x in radar.iter_elevation()]
   n = 0
   while n < len(elist)-1:
   
       if elist[n] == 720 and elist[n+1] == 720:
           radar.sweep_table.append((n, n+1))
           radar.reflectivity.append(n)
           radar.velocity.append(n+1)
           n += 2
           
       if elist[n] == 360:
           radar.sweep_table.append((n, n))
           radar.reflectivity.append(n)
           radar.velocity.append(n)
           n += 1

   print("\n Number of reflectivity levels:  %d" % len(radar.reflectivity))
   print("\n Number of radial velocity  levels:  %d\n" % len(radar.velocity))
   
   return True
########################################################################
# A wrapper for velocity unfolding...
  
def velocity_unfold(radar, unfold_type="region", gatefilter=None):

# In order to use pyART dealiasing, make sure the nyquist velocity on a sweep is constant 
# Multi-PRF schemes are a problem because the information needed to dealias is NOT stored in the
# Level-II file, as far as I know.
#
# For now, we are choosing the min nyquist.  This is a guess from looking at two cases, a supercell
# and a strong MCV having a lot of folding.

   nyq = radar.instrument_parameters['nyquist_velocity']['data'][...].copy()

   for idx in radar.iter_start_end():

       start = idx[0]
       end   = idx[1] + 1
       
       nyq_min = nyq[start:end].min()
       radar.instrument_parameters['nyquist_velocity']['data'][start:end] = nyq_min

   del(nyq)
    
# Dealias the velocity data

   if unfold_type == "region":

       dealiased_vel = pyart.correct.dealias_region_based(radar, interval_splits=3,
                                                          interval_limits=None, skip_between_rays=100,
                                                          skip_along_ray=100, centered=True,
                                                          nyquist_vel=None, check_nyquist_uniform=False,
                                                          gatefilter=None, rays_wrap_around=None,
                                                          keep_original=True, set_limits=False,
                                                          vel_field='velocity')
                                   
       radar.add_field('unfolded velocity', dealiased_vel)
       
       return True

   if unfold_type == "phase":
        
       dealiased_vel = pyart.correct.dealias_unwrap_phase(radar, unwrap_unit='sweep', 
                                                          nyquist_vel=None, 
                                                          check_nyquist_uniform=False, 
                                                          gatefilter=None, 
                                                          rays_wrap_around=None, 
                                                          keep_original=True, 
                                                          set_limits=False, 
                                                          skip_checks=True,
                                                          vel_field='velocity')

       radar.add_field('unfolded velocity', dealiased_vel)

       return True

   
#  Must implement function to get sounding data or specify previously unfolded radar 
#       volume to use PyART 4DD method. See PyART docs for more info.
#  if unfold_type == "4dd":  
#    snd_hgts,sngd_spds,snd_dirs = get_sound_data()
#    dealiased_radar = pyart.correct.dealias_fourdd(radar, last_radar=None, 
#                              sounding_heights=snd_hgts, sounding_wind_speeds=snd_spds, 
#                              sounding_wind_direction=snd_dirs, gatefilter=False, 
#                              filt=1, rsl_badval=131072.0, 
#                              keep_original=False, set_limits=True, 
#                              vel_field='velocity', corr_vel_field=None, 
#                              last_vel_field=None, debug=False, 
#                              max_shear=0.05, sign=1)

# If it gets here, there was a problem

   return False
########################################################################
# Texture defines a std deviation for a rolling window of length=LEN

def texture(input, radius=3, oneD=False):
    
# oneD flag is used to texture PhiDP along a radial, because it should NOT be a 2D texture
# input_array_dims = [az,range], so texture over second index
  
# ndimage cannot deal with masked arrays - but can deal with nan's - so replace bad values with nan's

    i2 = input.filled(fill_value=np.nan)
    
    if len(i2.shape) == 1 or oneD == True:
        kernel = np.ones((radius))/np.float(radius)
        kernel2 = kernel
    else:
        kernel = np.ones((radius,radius))/np.float(radius**2)
        kernel2 = kernel

    if len(i2.shape) == 2 and oneD == True:       
        std = np.empty_like(input)
        for n in np.arange(i2.shape[0]):
            avg    = scipy.ndimage.filters.convolve(i2[n], kernel2, mode='reflect', origin=0)
            dif    = i2[n] - avg
            c1     = scipy.ndimage.filters.convolve(dif,     kernel, mode='reflect', origin=0)
            c2     = scipy.ndimage.filters.convolve(dif*dif, kernel, mode='reflect', origin=0)
            std[n] = ((c2 - c1*c1)**.5)
    else:
        
        avg    = scipy.ndimage.filters.convolve(i2,      kernel2, mode='reflect', origin=0)
        dif    = i2 - avg
        c1     = scipy.ndimage.filters.convolve(dif,     kernel, mode='reflect', origin=0)
        c2     = scipy.ndimage.filters.convolve(dif*dif, kernel, mode='reflect', origin=0)
        std    = ((c2 - c1*c1)**.5)

    return np.ma.array(std, mask=np.isnan(std))

########################################################################
# Trap4 point

def trap4point( input, y1, y2, y3, y4):

   x1 = y1*np.ones(input.shape)

   x2 = y2*np.ones(input.shape)

   x3 = y3*np.ones(input.shape)

   x4 = y4*np.ones(input.shape)

   output = np.ma.zeros(input.shape)
   output.mask = input.mask
   
   mask1 = np.logical_and((input >= x2), (input <= x3))   
   output[mask1] = 1.0
    
   mask2 = np.logical_or((input < x1), (input > x4))
   output[mask2] = 0.0

   mask3 = np.logical_and((input > x1), (input < x2))
   tmp = (input-x1) / (x2-x1)
   output[mask3] = tmp[mask3]

   mask4 = np.logical_and((input > x3), (input < x4))
   tmp = (x4 - input) / (x4-x3)
   output[mask4] = tmp[mask4]
    
   return output

###########################################################################
# MetSignal:  Implementation of Krause's 2016 JTech QC algorithm in 1D/2D

def MetSignal(radar, sweep = 0, v_sweep = None):

# Fuzzy logic weights for filtering from Krause (2016)

   dbz_weight     = 2.0
   rhv_weight     = 1.0
   vel_weight     = 1.0
   std_zdr_weight = 2.0
   std_phi_weight = 2.0
   std_rhv_weight = 1.0
   FLT_MAX        = 1.0e8
   
   if v_sweep == None:
       v_sweep = radar.sweep_table[sweep][1]
    
   dbz = radar.get_field(sweep, 'reflectivity')
   zdr = radar.get_field(sweep, 'differential_reflectivity')
   phi = radar.get_field(sweep, 'differential_phase')
   rhv = radar.get_field(sweep, 'cross_correlation_ratio')
   vel = radar.get_field(v_sweep, 'velocity')
   
   metsignal = -10.0*np.ones(dbz.shape)
   
# Compute QC along each ray   

   for na in np.arange(dbz.shape[0]):
    
# Calculate the std-deviation for texture mapping

       std_phi = texture(phi[na])
       std_zdr = texture(zdr[na])
       std_rhv = texture(rhv[na])
       
       if _verbose_QC:
           print na, "PHI_STD: ", std_phi.max(), std_phi.min()
           print na, "ZDR_STD: ", std_zdr.max(), std_zdr.min()
           print na, "RHV_STD: ", std_rhv.max(), std_rhv.min()

       signal_value    = np.zeros(dbz.shape[1])
       signal_strength = np.zeros(dbz.shape[1]) 
       weight          = np.zeros(dbz.shape[1]) 
       sump            = np.zeros(dbz.shape[1], dtype=np.int) 
       
       signal_value = signal_value + dbz_weight*trap4point(dbz[na],10.0,30.0,FLT_MAX,FLT_MAX)
       weight       = weight + np.where(dbz[na].mask == False, dbz_weight, 0.0)
       sump         = sump + np.where(dbz[na].mask == False, 1, 0) 

       signal_value = signal_value + rhv_weight*trap4point(rhv[na],0.75, 0.9,FLT_MAX,FLT_MAX)
       weight       = weight + np.where(rhv[na].mask == False, rhv_weight, 0.0) 
       sump         = sump + np.where(rhv[na].mask == False, 1, 0) 

       signal_value = signal_value + 1.0 - vel_weight*trap4point(vel[na],-1.5, -1.0, 1.0, 1.5)
       weight       = weight + np.where(vel[na].mask == False, vel_weight, 0.0) 
       sump         = sump + np.where(vel[na].mask == False, 1, 0) 

       signal_value = signal_value + std_phi_weight*trap4point(std_phi,0.0, 0.0, 10., 20.)
       weight       = weight + np.where(std_phi.mask == False, std_phi_weight, 0.0) 
       sump         = sump + np.where(std_phi.mask == False, 1, 0) 
       
       signal_value = signal_value + std_zdr_weight*trap4point(std_zdr,0.0, 0.0, 1., 2.)
       weight       = weight + np.where(std_zdr.mask == False, std_zdr_weight, 0.0) 
       sump         = sump + np.where(std_zdr.mask == False, 1, 0) 
       
       signal_value = signal_value + std_rhv_weight*trap4point(std_rhv,0.0, 0.0, 0.02, 0.04)
       weight       = weight + np.where(std_rhv.mask == False, std_rhv_weight, 0.0) 
       sump         = sump + np.where(std_rhv.mask == False, 1, 0) 

# Locations with large amounts of Texture are non-meteorlogical while areas 
# with moderate to low amounts of texture are meteorlogical

       metsignal[na,:] = np.where(sump >= 4, np.floor(100.*signal_value/weight), -10)
    
# Hardlimits:  Asd some hard thresholds

# RhoHV < 0.65

   mask = np.logical_and((rhv < 0.65), (metsignal >= met_threshold))   
   metsignal = np.where(mask, -5.0, metsignal)

# Zdr < -4.5
   mask = np.logical_and((zdr  < -4.5), (metsignal >= met_threshold))   
   metsignal = np.where(mask, -5.1, metsignal)

# Zdr > 4.5
   mask = np.logical_and((zdr > 4.5), (metsignal >= met_threshold))   
   metsignal = np.where(mask, -5.2, metsignal)

# Add metsignal field to volume object

   return metsignal

    
########################################################################
# Volume Prep:  QC and field-based thresholding

def volume_prep(radar, QC_type = "Minimal", thres_vr_from_ref = False, max_range=150000.):

# Compute max gate to be used...

   max_range_gate = np.abs(radar.range['data'] - max_range).argmin()

# Mask data beyond max_range

   radar.fields['reflectivity']['data'][:,max_range_gate:] = np.ma.masked
   radar.fields['velocity']['data'][:,max_range_gate:] = np.ma.masked
   radar.fields['spectrum_width']['data'][:,max_range_gate:] = np.ma.masked
   radar.fields['cross_correlation_ratio']['data'][:,max_range_gate:] = np.ma.masked
   radar.fields['differential_reflectivity']['data'][:,max_range_gate:] = np.ma.masked
   radar.fields['differential_phase']['data'][:,max_range_gate:] = np.ma.masked

# Filter based on masking, dBZ threshold, and invalid gates

   gatefilter = pyart.correct.GateFilter(radar)
   gatefilter.exclude_invalid('velocity')
   gatefilter.exclude_invalid('reflectivity')
   gatefilter.exclude_masked('reflectivity')
  
   if QC_type == "None":
       return gatefilter

   if QC_type == "Minimal":

       for n, m in radar.sweep_table:
           ref_mask = (radar.get_field(n, 'reflectivity').data < _min_dbz)
           radar.get_field(n, 'reflectivity').mask = (radar.get_field(n, 'reflectivity').mask | ref_mask)                      
           if thres_vr_from_ref:
               ref_mask = radar.get_field(n, 'reflectivity').mask
               radar.get_field(m, 'velocity').mask = (((radar.get_field(m, 'velocity').mask | ref_mask) ) )

       return gatefilter
      
   elif QC_type == "MetSignal" or QC_type[0:3] == "Met":
  
       for n, m in radar.sweep_table:
           print("\n Processing sweep: %d " % n)
           metsignal = MetSignal(radar, sweep=n, v_sweep=n)
           metsig_vr_mask = (metsignal > _met_signal_mask_value['velocity']) 
           metsig_dbz_mask  = (metsignal > _met_signal_mask_value['reflectivity'])
           radar.get_field(n, 'reflectivity').mask = (radar.get_field(n, 'reflectivity').mask | metsig_dbz_mask)                      
           radar.get_field(m, 'velocity').mask     = (radar.get_field(m, 'velocity').mask | metsig_vr_mask) 

           radar.get_field(m, 'spectrum_width').data[...] = metsignal[...]
          
       return gatefilter

# This is my SIMPLEQC algorithm I put together, I think it works pretty well
# I use the dual-pol thresholds suggested by Krause, and then apply masks to the data fields.
#  

   else:  
  
       for n, m in radar.sweep_table:
      
           spw_mask  = (radar.get_field(m, 'spectrum_width').data > _spw_filter)
           ccr_mask  = (radar.get_field(n, 'cross_correlation_ratio').data < _rhv_filter )
           zdr_mask  = (radar.get_field(n, 'differential_reflectivity').data > _zdr_filter)
           ref_mask  = (radar.get_field(n, 'reflectivity').data < _min_dbz)

           if _verbose_QC: 
               print("\n SimpleQC:  ZdR   > thres:  %f  Number of gates removed:  %d" %( _zdr_filter, np.sum(zdr_mask == True)))
               print("\n SimpleQC:  RHOHV < thres:  %f  Number of gates removed:  %d" %( _rhv_filter, np.sum(ccr_mask == True)))
               print("\n SimpleQC:  SPWTH > thres:  %f  Number of gates removed:  %d" %( _spw_filter, np.sum(spw_mask == True)))   
               print("\n SimpleQC:  Number of valid DBZ gates before dual-pol masking:  %d  " % 
                         np.sum(radar.get_field(n, 'reflectivity').mask == False))
               print("\n SimpleQC:  Number of valid Velocity gates before dual-pol masking:  %d  " % 
                         np.sum(radar.get_field(m, 'velocity').mask == False))
   
           radar.get_field(n, 'reflectivity').mask = (((radar.get_field(n, 'reflectivity').mask) | ccr_mask) | zdr_mask | ref_mask)
   
           radar.get_field(n, 'reflectivity').mask = (((radar.get_field(n, 'reflectivity').mask) | ccr_mask) | zdr_mask | ref_mask)
           radar.get_field(m, 'velocity').mask     = (((radar.get_field(m, 'velocity').mask | spw_mask) | ccr_mask ) )

           if thres_vr_from_ref:
               ref_mask = radar.get_field(n, 'reflectivity').mask
               radar.get_field(m, 'velocity').mask = (((radar.get_field(m, 'velocity').mask | ref_mask) ) )

           if _verbose_QC: 
               print("\n SimpleQC:  Number of valid DBZ gates after dual-pol masking:  %d  " % 
                         np.sum(radar.get_field(n, 'reflectivity').mask == False))
               print("\n SimpleQC:  Number of valid Velocity gates after spectrum width masking:  %d \n" % 
                         np.sum(radar.get_field(m, 'velocity').mask == False))
  
# pyart.correct.despeckle.despeckle_field(radar, 'velocity', threshold=-100, size=10, gatefilter=gatefilter, delta=5.0)
# pyart.correct.despeckle.despeckle_field(radar, 'reflectivity', threshold=-100, size=100, gatefilter=gatefilter, delta=5.0)

       return gatefilter

