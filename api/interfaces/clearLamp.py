#!/usr/bin/env python

import unicornhat as unicorn
import psutil
import re

# only use as clean-up of lamp after killing processes
def cleanUp():
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(0.0)
    width,height=unicorn.get_shape()

    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x,y,int(0),int(0),int(0))
    unicorn.show()

def collectProcesses(processes):
    oldSession = False
    for process in psutil.process_iter():
        for string in process.cmdline():
            if re.search('pulse.py|banner.py|solid.py', string):
                oldSession=True
                processes.append(process)

    return oldSession, processes

def kill():
    processes = []
    oldSession, processes = collectProcesses(processes)

    print("clearLamp:kill: " + str(oldSession) + ", " + str(processes))

    if oldSession:
        for p in processes:
            p.terminate()
            p.wait()
            cleanUp()
            return 'off'

if __name__ == '__main__':
    kill()
    cleanUp()
