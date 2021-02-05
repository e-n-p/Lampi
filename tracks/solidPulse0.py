#!/usr/bin/env python

import math
import time
import unicornhat as unicorn
import sys

def spectrum(x,y):
    unicorn.set_pixel(x,y,int(255),int(0),int(255))

def wave(x,y):
    unicorn.set_pixel(x,y,int(220),int(20),int(60))

def run():

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(1)
    width,height=unicorn.get_shape()

    g = -1 
    while True:
        g += 1
        for y in range(height):
            for x in range(width):
                if x == g or x == g-1 or x == g-2:
                    wave(x,y)
                else:
                    spectrum(x,y)
                if g > 9:
                    g = -1

        unicorn.show()
        time.sleep(0.8)

if __name__ == "__main__":
    run()








