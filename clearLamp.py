#!/usr/bin/env python

import math
import time
import unicornhat as unicorn

def turnOff():

	unicorn.set_layout(unicorn.AUTO)
	unicorn.rotation(0)
	unicorn.brightness(0.0)
	width,height=unicorn.get_shape()

	for y in range(height):
		for x in range(width):
			unicorn.set_pixel(x,y,int(0),int(0),int(0))			
	unicorn.show()
