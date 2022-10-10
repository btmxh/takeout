#!/bin/bash
rm -rf Takeout
curl -o takeout.zip "$1" &&
unzip takeout.zip &&
rm takeout.zip