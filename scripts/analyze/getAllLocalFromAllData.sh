#!/bin/bash
########################### OLDDDD #################################

find ../../data | parallel --will-cite -j 4 './isLocal.sh < {} | grep local > /dev/null; r=$?; if (( r == 0 )); then echo {}; fi'
