# This script is finding files with the formats that defined as values in categories
# dictionary and move it to directories, that defined as keys of this dictionary. 

import os
import glob
import shutil

current_directory = os.getcwd()
categories = {
             'books':   ['*.txt', '*.doc', '*.fb2', '*.pdf', '*.djvu'],
             'music':   ['*.mp3', '*.wav', '*.flac'],
             'videos':  ['*.mkv', '*.mp4', '*.avi', '*.flv'],
             'pictures':['*.jpg', '*.png', '*.gif'],
             }

for pos in categories:
    if not os.path.isdir(pos):
        os.mkdir(pos)
    for x in range(len(categories[pos])):
        mask = glob.iglob(
                          os.path.join(current_directory, categories[pos][x])
                          )
        for name in mask:
            if os.path.isfile(name):
                shutil.move(name, pos)


