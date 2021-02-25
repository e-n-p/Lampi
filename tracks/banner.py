#!/usr/bin/env python

import time
import unicornhat as unicorn
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-bc", "--bcolour", required=False, help="Colour of background")
arg.add_argument("-wc", "--wcolour", required=False, help="Colour of wave")
arg.add_argument("-i", "--intensity", required=False, help="Brightness of lamp")
args = vars(arg.parse_args())

def background(x,y, background_colour):
    unicorn.set_pixel(x, y, background_colour[0], background_colour[1], background_colour[2])

def wave(x,y, wave_colour):
    unicorn.set_pixel(x, y, wave_colour[0], wave_colour[1], wave_colour[2])

def runBanner():

    intensity=1.0
    if args['intensity']:
        intensity = float(args['intensity'])
    background_colour = [255,0,255]
    if args['bcolour']:
        background_colour = list(map(int, args['bcolour'].split(",")))
    wave_colour = [220,20,60]
    if args['wcolour']:
        wave_colour = list(map(int, args['wcolour'].split(",")))

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(intensity)
    width,height=unicorn.get_shape()

    g = -1 
    while True:
        g += 1
        for y in range(height):
            for x in range(width):
                if x == g or x == g-1 or x == g-2:
                    wave(x, y, wave_colour)
                else:
                    background(x, y, background_colour)
                if g > 9:
                    g = -1

        unicorn.show()
        time.sleep(0.8)

if __name__ == "__main__":
    runBanner()

