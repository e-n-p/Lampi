#!/usr/bin/env python

import math
import unicornhat as unicorn

def main():
	run()

def run():
	width,height=unicorn.get_shape()

	for y in range(height):
		for x in range(width):
			unicorn.set_pixel(x,y,int(0),int(0),int(0))			
	unicorn.show()

if __name__ == "__main__":
	main()

