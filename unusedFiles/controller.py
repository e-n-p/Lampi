#!/usr/bin/env python

import os

trackNum = int(input())

if trackNum == 0:
	os.system('python solidPulse0.py')
elif trackNum == 1:
	solidPulse1
elif trackNum == 2:
	solidPulse2
else:
	print("Please select a valid track")

