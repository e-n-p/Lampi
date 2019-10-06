#!/usr/bin/env python

import math
import time
import unicornhat as unicorn

def main():
	controller("on")
	
def stop():
	width,height=unicorn.get_shape()
	print ("stop called")
	for y in range(height):
		for x in range(width):
			unicorn.set_pixel(x,y,int(0),int(0),int(0))
	unicorn.show()

def controller(signal):
	if signal == "on":
		print("run-signal-received")
		run(1)
	elif signal == "off":
		print("stop-signal-received")
		run(0)

def spectrum(x,y):
        unicorn.set_pixel(x,y,int(255),int(0),int(255))

def wave(x,y):
        unicorn.set_pixel(x,y,int(220),int(20),int(60))

def run(signal):

	unicorn.set_layout(unicorn.AUTO)
	unicorn.rotation(0)
	unicorn.brightness(0.6)
	width,height=unicorn.get_shape()

	#print("\n")
	#print("Running solidPulse")
	#print("\n")
	#time.sleep(.5)
	print(signal)
	g = -1 
	i = 0.0
	offset = 30
	while signal:
		i = i + 0.3
		g += 1
		for y in range(height):
			for x in range(width):
				#original(x,y,i,offset)
				if x == g-1 or x == g or x == g+1:
					wave(x,y)
				else:
					spectrum(x,y)
				if g > 7:
					g = -1 

		unicorn.show()
		time.sleep(0.8)

if __name__ == "__main__":
	main()
