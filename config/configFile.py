#!/usr/bin/env python

_grid_param = {
              'grid_spacing_xy' : 5000.,         # meters
              'domain_radius_xy': 150000.,       # meters
              'anal_method'     : 'Cressman',    # options are Cressman, Barnes (1-pass)
              'ROI'             : 5000./0.707,   # Cressman ~ analysis_grid * sqrt(2), Barnes ~ largest data spacing in radar
              'min_count'       : 6,             # regular radar data ~3, high-res radar data ~ 10
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

# Dict for the standard deviation of obs_error for reflectivity or velocity (these values are squared when written to DART) 
           
_obs_errors = {
              'reflectivity'  : 5.0,
              '0reflectivity' : 5.0, 
              'velocity'      : 3.0
              }

# Parameter dict setting radar data parameters
               
_radar_parameters = {
                    'min_dbz_analysis': 10.0, 
                    'max_range': 150000.,
                    'max_Nyquist_factor': 2,                    # dont allow output of velocities > Nyquist*factor
                    'field_label_trans': [False, "DBZC", "VR"]  # RaxPol 31 May - must specify for edit sweep files
                       }

def getConfig(dict,key):
    str = "%s['%s']" % (dict, key)
    print str
    param = eval(str)
    return param
