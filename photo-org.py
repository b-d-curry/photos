import os, time, shutil


topdir = '/volume1/media/Pictures/To Be Sorted/'
destdir = '/volume1/media/Pictures/Sorted'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        #Identify files to skip
        if '@eaDir' in dirpath:
            continue
        if name.casefold() == 'Thumbs.db'.casefold() or name.casefold() == '.picasa'.casefold() or name.casefold() == '.picasa.ini'.casefold():
            continue
        # Now identify the filename (used to decide if video or not)
        filename        = os.path.join(dirpath, name)
        (basename,ext) = os.path.splitext(name)
        # Calculate the timestamp, we'll use the older of creation vs modified
        fctime    = os.path.getctime(filename)
        fmtime    = os.path.getmtime(filename)
        ftime     = fctime if fctime < fmtime else fmtime
        timestamp = time.ctime(ftime)
        # Get the filesize to calculate duplicates
        fsize     = os.path.getsize(filename)
        # Now create a naming convention for the destination
        folder    = time.strftime("%Y", time.localtime(ftime))
        subfolder = time.strftime("%Y - %b", time.localtime(ftime))
        destpath  = os.path.join(destdir, folder, subfolder, name)
        linkpath  = os.path.join(destdir, 'Videos', folder, subfolder, name)
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
        print("Copying to: " + destpath)
        shutil.copy2(filename, destpath)
        # If its a Video file, then also create a symbolic link in the Videos dir tree
        #if ext.casefold() == '.MTS'.casefold() or ext.casefold() == '.MOV'.casefold() or ext.casefold() == '.MP4'.casefold() or ext.casefold() == '.MPG' or ext.casefold() == '.M4V':
            #os.makedirs(os.path.dirname(linkpath), exist_ok=True)
            #print("Making a link: " + linkpath)
            #os.symlink(destpath, linkpath)


