#!/bin/bash

file=$1
word=$2

if [ ! -f "$file" ]; then
    echo "File does not exist."
    exit 1
fi

count=$(grep -o -i "\b$word\b" "$file" | wc -l)
echo "The word '$word' occurs $count times in '$file'."
