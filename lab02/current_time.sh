#!/bin/bash

current=$(date +"%H:%M")
end_hour=18
end_minute=0

current_hour=$(date +"%H")
current_minute=$(date +"%M")
remaining_minutes=$(( (end_hour - current_hour) * 60 + (end_minute - current_minute) ))

hours=$((remaining_minutes / 60))
minutes=$((remaining_minutes % 60))

echo "Current time: $current. Work day ends after $hours hours and $minutes minutes."
