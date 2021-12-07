"""
    banner
"""
import time
import argparse

import unicornhat as unicorn

arg = argparse.ArgumentParser()
arg.add_argument("-bc", "--bcolour", required=False, help="Colour of background")
arg.add_argument("-wc", "--wcolour", required=False, help="Colour of wave")
arg.add_argument("-i", "--intensity", required=False, help="Brightness of lamp")
args = vars(arg.parse_args())

def background(x_coord, y_coord, bg_colour):
    unicorn.set_pixel(x_coord, y_coord, bg_colour[0], bg_colour[1], bg_colour[2])

def wave(x_coord, y_coord, wave_colour):
    unicorn.set_pixel(x_coord, y_coord, wave_colour[0], wave_colour[1], wave_colour[2])

def run_banner():

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
    width, height = unicorn.get_shape()

    wave_front = -1
    while True:
        wave_front += 1
        for y_coord in range(height):
            for x_coord in range(width):
                if x_coord in (wave_front, wave_front - 1, wave_front - 2):
                    wave(x_coord, y_coord, wave_colour)
                else:
                    background(x_coord, y_coord, background_colour)
                if wave_front > 9:
                    wave_front = -1

        unicorn.show()
        time.sleep(0.8)

if __name__ == "__main__":
    run_banner()
