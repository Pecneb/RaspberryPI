#!/bin/bash

# This script starts the camera module and the gpio module. 
python3 src/src_cam/main.py --input /dev/video0 &
python3 src/server.py
