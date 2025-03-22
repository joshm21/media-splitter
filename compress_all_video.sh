#!/bin/bash

# Loop through all .mp4 files in the current directory
for file in *.mp4; do
    # Run ffmpeg to compress the video
    ffmpeg -i "$file" \
        -vf "scale=-2:360" \    # Rescale the video to 360p (keeping aspect ratio)
        -b:v 800k \             # Set video bitrate to 800k
        -r 30 \                 # Set frame rate to 30 fps
        -c:v libx264 \          # Use x264 codec for video
        -preset slow \          # Slow encoding preset (better compression)
        -crf 23 \               # Constant Rate Factor for quality control (lower is better)
        -c:a aac \              # Use AAC codec for audio
        -b:a 128k \             # Set audio bitrate to 128k
        -movflags +faststart \  # Optimize for streaming (place metadata at the start)
        "${file%.mp4}_compressed.mp4"  # Output file in the current directory
done

