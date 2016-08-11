import os, shutil, glob

current_directory = os.getcwd()
categories = {'books':['*.txt','*.doc','*.fb2'],
              'music':['*.mp3','wav'],
              'pictures':['*.jpg','*.png','*.gif']}



for pos in categories:
    if not os.path.isdir(pos):
        os.mkdir(pos)
    for x in range(len(categories[pos])):
        mask = glob.iglob(os.path.join(current_directory, categories[pos][x]))
        for name in mask:
            if os.path.isfile(name):
                shutil.move(name, pos)


