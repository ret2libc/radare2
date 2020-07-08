import os
import shutil
import sys

srcdir = sys.argv[1]
try:
    os.mkdir(os.path.join(srcdir, "subprojects"))
except FileExistsError:
    pass

subprojects = ['spp', 'sdb']
for proj in subprojects:
    try:
        shutil.copy(os.path.join(srcdir, "shlr", proj), os.path.join(srcdir, "subprojects", proj))
    except FileExistsError:
        pass
