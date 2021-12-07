"""
    solid
"""
import argparse

import unicornhat as unicorn

arg = argparse.ArgumentParser()
arg.add_argument("-c", "--colour", required=False, help="Colour of Lamp")
arg.add_argument("-i", "--intensity", required=False, help="Brightness of lamp")
args = vars(arg.parse_args())

def set_LED(x_coord, y_coord, bg_colour):
    unicorn.set_pixel(x_coord, y_coord, bg_colour[0], bg_colour[1], bg_colour[2])

def run_solid():
    intensity=1.0
    if args['intensity']:
        intensity = float(args['intensity'])
    colour = [255,0,255]
    if args['colour']:
        colour = list(map(int, args['colour'].split(",")))

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(intensity)
    width,height=unicorn.get_shape()

    while True:
        for y_coord in range(height):
            for x_coord in range(width):
                set_LED(x_coord, y_coord, colour)

        unicorn.show()

if __name__ == "__main__":
    run_solid()
