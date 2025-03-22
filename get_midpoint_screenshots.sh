#!/bin/bash

for file in *.mp4; do
    # Get the duration and ensure it's a valid number
    duration=$(ffprobe -i "$file" -show_entries format=duration -v quiet -of csv="p=0")

    # Convert duration to an integer (fallback to 1 if something goes wrong)
    mid_time=$(awk -v d="$duration" 'BEGIN {print (d > 1) ? int(d / 2) : 1}')

    # Extract a frame from the middle timestamp and resize it
    output="${file%.mp4}.jpg"
    ffmpeg -y -ss "$mid_time" -i "$file" -vf "scale='if(gt(iw,ih),400,-1)':'if(gt(ih,iw),400,-1)'" -vframes 1 "$output"
    
    echo "Saved screenshot: $output"
done

