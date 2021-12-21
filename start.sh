#!/bin/bash

mkdir running
python3 src/src_cam/main.py --input /dev/video0 &
_camPID=$!
echo "$_camPID" > ./running/cam.pid
echo "$_camPID"
python3 web/webserver.py &
_webPID=$!
echo "$_webPID" > ./running/webserver.pid
echo "$_webPID"
python3 src/server.py
