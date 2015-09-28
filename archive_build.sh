#!/bin/sh
TODAY=$(date)
HOST=$(hostname)
echo "-----------------------------------------------------"
echo "Date: $TODAY                     Host:$HOST"
echo "-----------------------------------------------------"
# add rest code...
python archive_build.py
