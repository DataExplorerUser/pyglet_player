# Pyglet video player
Minimal example of playing an MP4 video with Pyglet using FFMPEG.

# FFMPEG
The FFMPEG files can be downloaded here.
https://github.com/BtbN/FFmpeg-Builds/releases

Download  ffmpeg-master-latest-win64-gpl-shared.zip

Pyglet 2.0.8 supports FFMPEG version 4,5 and 6.

# Installation
After downloading the ffmpeg zip file, unzip the file, preferable with 7-ZIP. Using 7-ZIP, you avoid the mark of the web on Windows, which may avoid anti-virus blocking the use of the files.

Copy the dll files from the `bin` folder over `lib` folder of ffmpeg.

Copy the resulting `lib` folder to the folder of `main.py`. When running `main.py` it should be able to use on the ffmpeg ddl's.

# Pyglet media installation documentation
https://pyglet.readthedocs.io/en/latest/programming_guide/media.html
