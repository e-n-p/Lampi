#!/bin/sh

#PIDs=()


ps -aux | grep solidPulse 
ps -aux | grep solidPulse | awk '{printf "%s ",$2}' 


kill $( ps -aux | grep solidPulse | awk '{$2}' )
#ps -aux | grep solidPulse | awk '{printf "%s ",$2}' 


