#!/usr/bin/env python

import psutil
from subprocess import Popen
import clearLamp

oldSession = False
processes = []
for process in psutil.process_iter():
	if any('banner' in string for string in process.cmdline()):
		oldSession=True
		processes.append(process)

if oldSession:
	for p in processes:
		p.terminate()
		p.wait()
		clearLamp.turnOff()
else:
	Popen(['python', 'banner.py'], cwd='/home/pi/server/tracks/')
