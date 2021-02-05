#!/usr/bin/env python

import time
import unicornhat as unicorn

def pulse(x,y):
    unicorn.set_pixel(x,y,int(220),int(20),int(60))

def run():

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(1)

    program = [ [3,5],
                [2,6],
                [1,7],
                [0,8],
                [1,7],
                [2,6] ]

    controller = 0
    while True:
        unicorn.clear()
        topLeft, extent = program[controller]
        for y in range(topLeft, extent):
            for x in range(topLeft, extent):
                pulse(x,y)

        unicorn.show()
        time.sleep(0.5)
        if controller <= 4:
            controller += 1
        else:
            controller = 0


if __name__ == "__main__":
    run()

