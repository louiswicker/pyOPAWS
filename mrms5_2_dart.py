#!/usr/bin/env python

import time
import os
import sys
import datetime
import subprocess

_MRMS_top_dir            = "/work/john.krause/realtime"
_MRMS_bin                = "/work/john.krause/bin"
_NEWSe_bin               = "/work/wicker/REALTIME/pyroth"
_NEWSe_top_dir           = "/work/wicker/REALTIME/"
_NEWSe_grid_info         = "/scratch/wof/realtime/radar_files"
#
#-------------------------------------------------------------------------------
#
_MRMS_input_dir          = os.path.join(_MRMS_top_dir, "grid/output")
_MRMS_obs_seq_dir        = os.path.join(_MRMS_top_dir, "")
_MRMS_grid_config_file   = os.path.join(_MRMS_top_dir, "grid_config.txt")
_MRMS_radar_config_file  = os.path.join(_MRMS_top_dir, "radarinfo.dat")
_MRMS_Init_Docker_exe    = [os.path.join(_MRMS_bin, "initRadar3DGrid.pl"), "-v", "-d", _MRMS_top_dir, "-r"]
_MRMS_Grid_Setup_exe     = [os.path.join(_MRMS_bin, "Radar3DGrid_Driver"), "-q", "-c", _MRMS_grid_config_file]
_MRMS_Grid_Driver_exe    = [os.path.join(_MRMS_bin, "Radar3DGrid_Driver.cmd")]
_MRMS_Grid_MsgMaker_exe  = [os.path.join(_MRMS_bin, "Radar3DGrid_MsgMaker.cmd")]
_MRMS_Kill_All_exe       = [os.path.join(_MRMS_bin, "initRadar3DGrid"), "-s"]

_MRMS_log_files          = [os.path.join(_MRMS_top_dir, "log_Docker.txt"), \
                            os.path.join(_MRMS_top_dir, "log_GridD.txt"),  \
                            os.path.join(_MRMS_top_dir, "log_MsgM.txt"),   \
                            os.path.join(_MRMS_top_dir, "log_KillAll.txt")]

_NEWSe_grid_prep_exe     = [os.path.join(_NEWSe_top_dir, "pyroth/prep_grid3d.py")]
_NEWSe_log_files         = [os.path.join(_NEWSe_top_dir, "log_grid_prep.txt")]

debug = False

#-------------------------------------------------------------------------------
# Utility to round the datetime object to nearest 15 min....

def quarter_datetime(dt):
    minute = (dt.minute//15)*15
    return dt.replace(minute=0, second=0)+datetime.timedelta(minutes=minute)

#-------------------------------------------------------------------------------
def run_MRMS_Programs(Init_Dockers):

    print("\n============================================================================")
    print("\n MRMS_programs will now start the executables need for radar REF processing")

    print("\n Starting docker programs ")
    with open(_MRMS_log_files[0], 'w') as fp0:
        p = subprocess.Popen(Init_Dockers, stdout=fp0)

    print("\n Starting Grid_Driver program")
    os.system("cp %s %s" % ("./Radar3DGrid_Driver.cmd", _MRMS_Grid_Driver_exe[0]))
    os.chmod(_MRMS_Grid_Driver_exe[0],0775)
    with open(_MRMS_log_files[1], 'w') as fp1:
        p = subprocess.Popen(_MRMS_Grid_Driver_exe, stdout=fp1, shell=True)

    print("\n Starting MsgMaker program")
    os.system("cp %s %s" % ("./Radar3DGrid_MsgMaker.cmd", _MRMS_Grid_MsgMaker_exe[0]))
    os.chmod(_MRMS_Grid_MsgMaker_exe[0],0775)
    with open(_MRMS_log_files[2], 'w') as fp2:
        p = subprocess.Popen(_MRMS_Grid_MsgMaker_exe, stdout=fp2, shell=True)

    print("\n Now everything should be running to create NEWSe MRMS files.....")
    print("\n============================================================================")

#-------------------------------------------------------------------------------
def run_MRMS_Setup():

    print("\n============================================================================")
    print("\n MRMS_Setup is using the list:  %s" % _MRMS_Grid_Driver_exe)
    print("\n============================================================================")

    p = subprocess.Popen(_MRMS_Grid_Setup_exe, stdout=subprocess.PIPE)
    file_txt = p.communicate()[0]
    print file_txt

    if debug:
        f = open("Grid_Setup_DEBUG.txt", "w")
        f.write(file_txt)
        f.close()

# Write out the radars file

    txt = file_txt.split('\n')
    print txt
    start = txt.index("Recommeded radarinfo file:") + 1
    end   = len(txt) - 1 #blank line in output

    Init_Docker_list = _MRMS_Init_Docker_exe
    radars = ""
    f = open(_MRMS_radar_config_file,"w")
    for item in txt[start:end]:
        print item
        f.write("%s\n" % item)
        radars = ("%s%s," % (radars, item[0:4]))
    f.close()
    Init_Docker_list.append(radars)

# Now create the string needed for the
    return Init_Docker_list

#-------------------------------------------------------------------------------
def create_MRMS_grid(day=None):

# create path for NEWSe radar file

    if day == None:
        day = time.strftime("%Y%m%d")

    radar_csh_file = os.path.join(_NEWSe_grid_info, ("radars.%s.csh" % day))

# Parse center lat and lon out of the c-shell radar file - HARDCODED!
# If the file does not exist, then we exit out of this run

    try:
        fhandle = open(radar_csh_file)
    except:
        print("\n============================================================================")
        print("\n CANNOT OPEN radar CSH file, exiting MRMS processing:  %s" % radar_csh_file)
        print("\n============================================================================")
        sys.exit(1)

    all_lines  = fhandle.readlines()
    lat = float(all_lines[7].split(" ")[2])
    lon = float(all_lines[8].split(" ")[2])
    fhandle.close()

    print("\n============================================================================")
    print("\n create_MRMS_grid_config writing Lat: %f  Lon: %f to grid_config file" % (lat, lon))
    print("\n============================================================================")

    file_txt = """
#
# Automatically generated by Python
#
#Config File for Radar3DGrid
#Note only a single space is allowed between
#variable name and value
CENTER_LAT %10.6f
CENTER_LON %10.6f
#
LAT_SPACING_DEG 0.0500
LON_SPACING_DEG 0.0500
#
#west_east 
NUM_X 180
#North-South
NUM_Y 180
#up down
NUM_Z 20
#
Z_RES_METERS 500.0
#
TIME_CUTOFF_SECONDS 720
MAX_NUM_RADARS_PER_GRIDPOINT 3
MAX_RADAR_DISTANCE_KM 300.0
#
#
RADAR_INFO_FILE /work/john.krause/realtime/radarinfo.dat
INPUT_MSG_DIR /work/john.krause/realtime/grid/msg
OUTPUT_DIR /work/john.krause/realtime/grid/output
#
XY_RADIUS_METERS 2000.0
Z_RADIUS_METERS  1500.0""" % (lat, lon)

    f = open(_MRMS_grid_config_file, "w")
    f.write(file_txt)
    f.close()

#-------------------------------------------------------------------------------
def kill_MRMS_Programs():

    print("\n============================================================================")
    print("\n Shutting down all the MRMS programs")

    print("\n Starting Grid_Driver program")
    with open(_MRMS_log_files[3], 'w') as fp10:
        p = subprocess.Popen(_MRMS_Kill_All_exe, stdout=fp10)

#   os.system('pkill '+)
    print("\n Hopefully this worked.....")
    print("\n============================================================================")


#-------------------------------------------------------------------------------
def run_Prep_Grid3d(today):

    obs_seq_out_dir = os.path.join(_MRMS_obs_seq_dir, today)

    gmt = time.gmtime()  # for file names, here we need to use GMT time

    dt = quarter_datetime(datetime.datetime(*gmt[:6]))

    str_time = dt.strftime("%Y%m%d%H%M")

    cmd = "prep_grid3d.py -d %s -w -o %s --realtime %s -p 4" % (_MRMS_input_dir, obs_seq_out_dir, str_time)

    print("\n Prep_Grid3d running job: at %s" % (time.strftime("%Y-%m-%d %H:%M:%S")))
    print("\n %s" % cmd)
    print("\n %s" % gmt)
    print("\n %s" % str_time)

#-------------------------------------------------------------------------------
def run_Prep_MRMS(obs_seq_out_dir, time):
    """
      obs_seq_out_dir:  the directory to dump files into
      time:             datetime object which includes what GMT time

    call looks like:  prep_mrms.py -d /work/LDM/MRMS/2017/04/20 -w -o /work/wicker/REALTIME/20170419 --realtime 201704200215 -p 3 --loc 41.109259 -94.913899

    """

    dt = quarter_datetime(time)

    str_time = dt.strftime("%Y%m%d%H%M")

    cmd = "prep_grid3d.py -d %s -w -o %s --realtime %s -p 4" % (_MRMS_input_dir, obs_seq_out_dir, str_time)

    print("\n Prep_Grid3d running job: at %s" % (time.strftime("%Y-%m-%d %H:%M:%S")))
    print("\n %s" % cmd)
    print("\n %s" % gmt)
    print("\n %s" % str_time)

    os.system("%s >> %s" % (cmd, _NEWSe_log_files[0]))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Main program

def run_MRMS(argv=None):

# First call parses the radar.YYYYMMDD.csh file in the NEWSe_real-time directory
#       and then creates the grid_config.txt file in the MRMS_real-time directory

    create_MRMS_grid()

# Second call parses the radar information from running Radar3DGrid_Driver into the
#       radarinfo.dat file in the MRMS real-time directory...it returns the command
#       needed to run the DOCKER containers which has a list of radars on the end of it

    docker_list = run_MRMS_Setup()

# Finally, this call runs all the programs, and starts the prep_grid3d.py code to convert
#       the netCDF4 files that MRMS creates into obs_seq.out files for DART

    run_MRMS_Programs(docker_list)

#-------------------------------------------------------------------------------
# Main program 
#
if __name__ == "__main__":
    sys.exit(run_MRMS())
