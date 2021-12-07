"""
    pulse
"""
import time
import argparse

import unicornhat as unicorn

arg = argparse.ArgumentParser()
arg.add_argument("-c", "--colour", required=False, help="Colour of pulse")
arg.add_argument("-i", "--intensity", required=False, help="Colour of wave")
args = vars(arg.parse_args())

def pulse(x_coord, y_coord, colour):
    unicorn.set_pixel(x_coord, y_coord, colour[0], colour[1], colour[2])

def run_pulse():
    intensity=1.0
    if args['intensity']:
        intensity = float(args['intensity'])
    colour = [255,0,255]
    if args['colour']:
        colour = list(map(int, args['colour'].split(",")))

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(intensity)

    program = [
        [3,5],
        [2,6],
        [1,7],
        [0,8],
        [1,7],
        [2,6]
    ]

    controller = 0
    while True:
        unicorn.clear()
        top_left, extent = program[controller]
        for y_coord in range(top_left, extent):
            for x_coord in range(top_left, extent):
                pulse(x_coord, y_coord, colour)

        unicorn.show()
        time.sleep(0.5)
        if controller <= 4:
            controller += 1
        else:
            controller = 0


if __name__ == "__main__":
    run_pulse()
