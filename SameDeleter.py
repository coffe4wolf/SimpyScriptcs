# This script is deleting the same files in directory wehre
# the script is placed.
import os
import filecmp

cur_dir = os.getcwd()
files = os.listdir(cur_dir)                   # getting the list of files in directory
del_list = []

for i in range(len(files)):
    try:
        if filecmp.cmp(files[i],files[i+1]):  # comparing nearby elements of files list
            del_list.append(files[i])         # pull one of it if are the same
    except IndexError:
         pass
for j in del_list:
    os.remove(j)

