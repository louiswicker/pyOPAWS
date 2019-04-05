#!/usr/bin/env python


import time
import logging
import os, sys
import datetime

# RunIt turns on and off actually doing something
RunIt = True

_WSR88D_feed     = "/work/LDM/NEXRAD2"
_WSR88D_obs_seq  = "/work/wicker/REALTIME/VR"
_NEWSe_grid_info = "/scratch/wof/realtime/radar_files"
_NEWSe_grid_info = "./"
_opaws2D         = "/work/wicker/realtime/pyOPAWS/opaws2d.py"

# Cressman parameters
_dx  = 5000.
_roi = 1000.

# Plot this level
_plot_level = 3

year       = 2019
mon        = 4
day        = [5, 5]   # start and stop days
hour       = [22, 22]    # start and stop hours
mmin       = [30, 30]

start_time = datetime.datetime(year, mon, day[0], hour[0], mmin[0], 0)
stop_time  = datetime.datetime(year, mon, day[1], hour[1], mmin[1], 05)
dtime      = datetime.timedelta(minutes=15)

_obs_seq_out_dir = os.path.join(_WSR88D_obs_seq, start_time.strftime("%Y%m%d"))

# create path for NEWSe radar file

radar_file_csh = os.path.join(_NEWSe_grid_info, ("radars.%s.csh" % start_time.strftime("%Y%m%d")))

# Parse center lat and lon out of the c-shell radar file - HARDCODED!
# If the file does not exist, then we exit out of this run

try:
    fhandle = open(radar_file_csh)
except:
    print("\n ============================================================================")
    print("\n CANNOT OPEN radar CSH file, exiting WSR88D processing:  %s" % radar_csh_file)
    print("\n ============================================================================")
    sys.exit(1)

# Read radars out of radars.YYYYMMDD file

fhandle    = open(radar_file_csh)
all_lines  = fhandle.readlines()
radar_list = all_lines[6].split("(")[1].split(")")[0].split()
fhandle.close()

radar_list = ['KMAF']

while start_time < stop_time:

    print start_time.strftime("%Y,%m,%d,%H,%M")

    for radar in radar_list:
        print("\n ============================================================================")
        print("\n Radar: %s  is being processed " % (radar))
        print("\n ============================================================================")

# Main catchup loop

        WSR88D_dir = os.path.join(_WSR88D_feed, radar)
    
        print("\n Reading from operational WSR88D directory:  %s\n" % WSR88D_dir)

# Do one radar for a test
# opaws2d.py -p 1 -o $outdir -d $indir -w --window 2018,05,02,23,45 --onlyVR --dx 5000. --roi 5000.
    
        print("\n >>>>=======BEGIN===============================================================")
        cmd = "%s -d %s -o %s -w --window %s -p %d --onlyVR --dx %f  --roi %f"  %  \
              (_opaws2D, WSR88D_dir, _obs_seq_out_dir, start_time.strftime("%Y,%m,%d,%H,%M"), _plot_level, _dx, _roi)

        print("\n opaws2D called at %s" % (time.strftime("%Y-%m-%d %H:%M:%S")))

        print(" Cmd: %s" % (cmd))

        if RunIt:  
            ret = os.system("%s" % cmd)
        else:
            ret = 0

        if ret != 0:
            print("\n ============================================================================")
            print("\n opaws2D cannot find a RF file between [-2,+1] min of %s" % start_time.strftime("%Y%m%d%H%M"))
            print("\n ============================================================================")
        print("\n <<<<<=======END================================================================")

    start_time = start_time + dtime
