. "./config"

ffmpeg -f flv -listen 1 -i "$source_path" -an -c:v copy -b:v 500k -ldash 1 -streaming 1 -use_template 1 -use_timeline 0 -seg_duration "$segment_duration" -remove_at_exit 1 -f dash "$output_path"