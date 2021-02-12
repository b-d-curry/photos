import os, time, shutil


topdir = '/volume1/media/Pictures/'
destdir = '/volume1/media/Pictures/'

for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        #Identify files to skip
        if '@eaDir' in dirpath or 'Videos' in dirpath:
            continue
        if name.casefold() == 'Thumbs.db'.casefold() or name.casefold() == '.picasa'.casefold() or name.casefold() == '.picasa.ini'.casefold():
            continue
        # Now identify the filename (used to decide if video or not)
        filename       = os.path.join(dirpath, name)
        (basename,ext) = os.path.splitext(name)
        # Calculate the timestamp, we'll use the older of creation vs modified
        fctime    = os.path.getctime(filename)
        fmtime    = os.path.getmtime(filename)
        ftime     = fctime if fctime < fmtime else fmtime
        timestamp = time.ctime(ftime)
        # Now create a naming convention for the destination
        folder    = time.strftime("%Y", time.localtime(ftime))
        subfolder = time.strftime("%Y - %b", time.localtime(ftime))
        linkpath  = os.path.join(destdir, 'Videos', folder, subfolder, name)
        if (os.path.exists(linkpath)):
            print("Skipping duplicate: " + linkpath)
            continue
        # If its a Video file, then also create a symbolic link in the Videos dir tree
        if ext.casefold() == '.MTS'.casefold() or ext.casefold() == '.MOV'.casefold() or ext.casefold() == '.MP4'.casefold():
            os.makedirs(os.path.dirname(linkpath), exist_ok=True)
            print("Making a link: " + linkpath)
            os.symlink(filename, linkpath)


