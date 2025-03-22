# media-splitter
A utility to play audio/video, add split points, name each split, and export the data.

# how it works
1. download the media-splitter.html file
2. open it in your browser
3. load your audio/video file (nothing is uploaded to a remote server)
4. use the "Play" button to start the media file
5. press "Split" whenever you want to add a split point
7. repeat steps 4 and 5 as needed
8. (optional) rename, play, or delete a split in the "Splits" table 
10. press the "Save as CSV" button
11. You can use this file with another tool to actually split apart the media file
    - look into [ffmpeg](https://www.ffmpeg.org/)
    - ai is your friend; see this project's python/bash scripts generated by ai to parse the csv's and split the media files
