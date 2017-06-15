#!/usr/bin/env python

import os

# remove all module files in directory - this can trip you up bad!

print "\n=====================================================\n"
print("   ---> Removing all module files...safety first!")
print "\n=====================================================\n"

cmd = "f2py --fcompiler='gnu95' --f90flags='-O3' -c -m cressman cressman.f90"
os.system(cmd)
#cmd = "f2py --fcompiler='gnu95' --f90flags='-O3' -c -m cressman kdtree2.o cressman.f90"
#os.system(cmd)
