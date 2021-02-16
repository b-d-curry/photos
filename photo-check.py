"""
"""
import os, time, shutil
import datetime
import re

topdir = '/volume1/media/Pictures/'
destdir = '/volume1/media/Pictures/'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        #Identify files to skip
        if '@eaDir' in dirpath:
            continue
        if name.casefold() == 'Thumbs.db'.casefold() or name.casefold() == '.picasa'.casefold() or name.casefold() == '.picasa.ini'.casefold():
            continue
        #print(dirpath)
        match = re.search('(\d{4})\/(\d{4}) - (\w{3})$', dirpath)
        if not match:
            #print("Skipping:",dirpath)
            continue
        filename       = os.path.join(dirpath, name)
        (basename,ext) = os.path.splitext(name)
        match = re.search('(\w+)_(\d{4})(\d{2})(\d{2})_(\w+)',basename)
        if match:
            months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
            folder = match.group(2)
            subfolder = folder + " - " + months[int(match.group(3))]
            #print(filename)
            #print(subfolder)
            if folder+"/"+subfolder not in filename:
                #print("Wrong ",filename,"should be",subfolder)
                destpath = os.path.join(destdir, folder, subfolder, name)
                # Get the filesize to calculate duplicates
                fsize    = os.path.getsize(filename)
                # If the destination already exists and is of the same file size, then skip it
                if (os.path.exists(destpath) and fsize == os.path.getsize(destpath)):
                    print("Skipping duplicate ",filename)
                    continue
                # Now check for unique naming, add _n until we get to a unique name
                findex = 0
                while (os.path.exists(destpath)):
                    findex = findex + 1
                    destpath = os.path.join(destdir, folder, subfolder, basename+'_'+str(findex)+ext)
                    linkpath = os.path.join(destdir, 'Videos', folder, subfolder, basename+'_'+str(findex)+ext)
                    print("Renaming destpath: " + destpath)
                # Make the destination directory and copy the file across
                os.makedirs(os.path.dirname(destpath), exist_ok=True)
                print("Moving to: " + destpath)
                shutil.move(filename, destpath)
