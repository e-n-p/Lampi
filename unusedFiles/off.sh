#!/bin/bash

ps -ef | grep "python" | grep solidPulse | awk '{print $2}' | xargs sudo kill | sudo python /home/pi/server/lampOff.py >/dev/null 2>&1


#ProcessToKill=$( ps -ef | grep 'python' | grep solidPulse | awk '{print $2}' )

#echo $ProcessToKill

