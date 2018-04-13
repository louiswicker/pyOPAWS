import os
import sys
from multiprocessing import Pool
from optparse import OptionParser

_default_NCKS = "/home/louis.wicker/anaconda2/bin/ncks"

_default_compression = 3

ncks_cmd = '%s --ovr -4 --ppc default=%d %s %s >> ncks.log'
nthreads = 5

#=======================================================================================================================
# RunMember is a function that runs a system command

def RunMember(cmd):
    print("\n Executing command:  %s " % cmd)
    os.system(cmd)
    print("\n %s completed...." % cmd)
    return


#=======================================================================================================================
# 
def get_all_files(rootdir, mindepth = 1, maxdepth = float('inf')):
    """
    Usage:

    d = get_all_files(rootdir, mindepth = 1, maxdepth = 2)

    This returns a list of all files of a directory, including all files in
    subdirectories. Full paths are returned.

    WARNING: this may create a very large list if many files exists in the 
    directory and subdirectories. Make sure you set the maxdepth appropriately.

    rootdir  = existing directory to start
    mindepth = int: the level to start, 1 is start at root dir, 2 is start 
               at the sub direcories of the root dir, and-so-on-so-forth.
    maxdepth = int: the level which to report to. Example, if you only want 
               in the files of the sub directories of the root dir, 
               set mindepth = 2 and maxdepth = 2. If you only want the files
               of the root dir itself, set mindepth = 1 and maxdepth = 1
    """
    rootdir = os.path.normcase(rootdir)
    file_paths = []
    root_depth = rootdir.rstrip(os.path.sep).count(os.path.sep) - 1
    for dirpath, dirs, files in os.walk(rootdir):
        depth = dirpath.count(os.path.sep) - root_depth
        if mindepth <= depth <= maxdepth:
            for filename in files:
                file_paths.append(os.path.join(dirpath, filename))
        elif depth > maxdepth:
            del dirs[:]  
    return file_paths

#=======================================================================================================================
# Main

# Process command lines

parser = OptionParser()

parser.add_option("-i",  "--input",  dest="srcDir", type="string", help = "Path to files needing to be compressed")
parser.add_option("-o",  "--output", dest="outDir", type="string", help = "Path to compressed directory")

(options, args) = parser.parse_args()

if options.srcDir == None:
    print("\n ==> compress_ncdf: ERROR --> No source directory specified!!!\n")
    parser.print_help()
    sys.exit(-1)
else:
    srcDir = options.srcDir
    print("\n ==> compress_ncdf: Reading files from directory %s\n" % srcDir)

if options.outDir == None:
    print("\n ==> compress_ncdf: ERROR --> No output directory specified!!!\n")
    print("\n ==> compress_ncdf: Creating a directory automatically!!\n")
    outDir = "%s_compressed" % srcDir
    print("\n ==> compress_ncdf: Writing files into directory %s\n" % outDir)
else:
    outDir = options.outDir
    print("\n ==> compress_ncdf: Writing files into directory %s\n" % outDir)


# body code

fileList = get_all_files(srcDir)

pool = Pool(processes=nthreads)              # set up a queue to run

for fname in fileList:

    if fname.count('fcst_end') == 0:
        # Construct new filename
        mystr = fname.split('/',4)
        newfname = os.path.join(outDir, mystr[-1])
        # check to see if new directory exists
        if not os.path.exists(os.path.dirname(newfname)):
            print("\nCreating new directory:  %s\n" % os.path.dirname(newfname))
            os.makedirs(os.path.dirname(newfname))
        cmd = ncks_cmd % (_default_NCKS, _default_compression, fname, newfname)
        pool.apply_async(RunMember, (cmd,))

pool.close()
pool.join()

