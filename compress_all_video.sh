#!/bin/bash

# Loop through all .mp4 files in the current directory
for file in *.mp4; do
    # Run ffmpeg to compress the video
    ffmpeg -i "$file" \
        -vf "scale=-2:360" \
        -b:v 800k \
        -r 30 \
        -c:v libx264 \
        -preset slow \
        -crf 23 \
        -c:a aac \
        -b:a 128k \
        -movflags +faststart \
        "${file%.mp4}_compressed.mp4"  # Output file in the current directory
done
