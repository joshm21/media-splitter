#!/bin/bash

# Get the total number of .mp4 files
total_files=$(ls *.mp4 | wc -l)
file_count=0

# Loop through all .mp4 files in the current directory
for file in *.mp4; do
    # Increment the file count
    file_count=$((file_count + 1))

    # Echo the current file number out of the total with a color
    echo -e "\033[1;32mProcessing file $file_count of $total_files: $file\033[0m"

    # Run ffmpeg to compress the video with reduced output verbosity
    ffmpeg -loglevel error -i "$file" \
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
