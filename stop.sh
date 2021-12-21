#!/bin/bash

PIDcam=$(<"./running/cam.pid")
echo "killing process $PIDcam"
kill -9 $PIDcam
PIDweb=$(<"./running/webserver.pid")
echo "killing process $PIDweb"
kill -9 $PIDweb
rm -r running
