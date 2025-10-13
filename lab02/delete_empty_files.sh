#!/bin/bash

dir=$1

if [ ! -d "$dir" ]; then
    echo "Directory does not exist."
    exit 1
fi

for file in "$dir"/*; do
    if [ -f "$file" ] && [ ! -s "$file" ]; then
        echo "Deleting empty file: $file"
        rm "$file"
    fi
done
