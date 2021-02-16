# photos
Scripts to organise our photos on the bloodybox

* photo-org.py - main script to organise photos from "To Be Sorted"
  * Now has a dependency on exiftool: https://exiftool.org/
  * Synology package for exiftool available from: https://www.cphub.net/?p=exiftool
  * Python wrapper around exiftool abailable from: https://github.com/smarnach/pyexiftool
* photo-merge.py - takes the photos organised by photo-org and merges them back into the main folder structure
* photo-dupes.py - used to find duplicates for removal
* video-link.py - creates symbolic links back to the original videos
