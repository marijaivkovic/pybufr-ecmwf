#!/usr/bin/env python

import os,glob,sys

# possible inputs:
# all [default]
# bufr
# f2py

arg='all'
num_args = len(sys.argv)
if (num_args> 1):
    arg = sys.argv[1]

# sanity check
allowed_args = ['all','bufr','f2py']
if (not arg in allowed_args):
    print "ERROR: invalid argument: ",arg
    print "Allowed arguments are: ",', '.join(a for a in allowed_args)
    sys.exit(1)

bufr_dirs_to_delete = ["ecmwf_bufr_lib/bufr_000380",
                       "ecmwf_bufr_lib/bufr_000371",
                       "ecmwf_bufr_lib/bufr_000381",
                       "tmp_BUFR_TABLES"]

f2py_dirs_to_delete = ["f2py_build"]

dirs_to_delete = []
if ((arg=='all') or (arg=='bufr')):
    dirs_to_delete.extend(bufr_dirs_to_delete)
if ((arg=='all') or (arg=='f2py')):
    dirs_to_delete.extend(f2py_dirs_to_delete)

backup_files_to_delete = glob.glob("*~")
bufr_files_to_delete =["libbufr.a",
                       "ecmwfbufr.so",
                       "ecmwf_bufr_lib/ConfigFile"]
f2py_files_to_delete = ["ecmwfbufr.so"]

files_to_delete = []
if ((arg=='all') or (arg=='bufr')):
    files_to_delete.extend(bufr_files_to_delete)
if ((arg=='all') or (arg=='f2py')):
    files_to_delete.extend(f2py_files_to_delete)

files_to_delete.extend(backup_files_to_delete)

for d in dirs_to_delete:
    if (os.path.exists(d)):
        print "deleting dir: ",d
        os.system(r"\rm -rf "+d)
    # this only works if the dirs are empty!
    #os.removedirs(d)

for f in files_to_delete:
    if (os.path.exists(f)):
        print "deleting file: ",f
        os.remove(f)
        #os.system(r"\rm -f "+f)
    if (os.path.islink(f)):
        print "deleting symlink: ",f
        os.remove(f)

print "done"
