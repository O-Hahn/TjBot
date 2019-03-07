#!/bin/bash
pids=$(ps -elf | grep "/home/pi/TJBot-python/pong.py" | head -n -1  | grep -oE ".*pi *[0-9]+" | grep -oE "[0-9]+$")
if [ "$pids" != "" ]; then
    while read -r pid; do
        if [ "$pid" = "" ]; then
            exit 0
        fi
        if [ "$pid" != "$1" ]; then
            echo "Killing $pid"
            kill -SIGKILL "$pid"
        fi
    done <<< "$pids"
fi


