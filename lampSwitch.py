#!/usr/bin/env python

from subprocess import Popen
from clearLamp import kill, collectProcesses


def lampSwitch():
    processes = []
    oldSession, _ = collectProcesses(processes)

    if oldSession:
        kill()
    else:
        Popen(['python', 'banner.py'], cwd='/home/pi/server/tracks/')
        return 'on'

if __name__ == '__main__':
    lampSwitch()