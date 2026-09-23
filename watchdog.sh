#!/bin/bash

disk_usage=$(df / | tail -1 | awk '{print $5}' | tr -d '%')


ram_total=$(free -m | awk '/^Mem:/ {print $2}')

ram_used=$(free -m | awk '/^Mem:/ {print $3}')

ram_usage=$((ram_used * 100 / ram_total))

echo "Disk usage: $disk_usage%"
echo "RAM usage: $ram_usage%"


if [ "$disk_usage" -gt 80 ]; then
    echo "WARNING: Disk usage is above 80%!"
fi

if [ "$ram_usage" -gt 80 ]; then
    echo "WARNING: Memory usage is above 80%!"
fi
