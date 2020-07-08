import os
import shutil
import sys

srcdir = sys.argv[1]
os.mkdir(os.path.join(srcdir, "subprojects"))

subprojects = ['spp', 'sdb']
for proj in subprojects:
    shutil.copy(os.path.join(srcdir, "shlr", proj), os.path.join(srcdir, "subprojects"))
