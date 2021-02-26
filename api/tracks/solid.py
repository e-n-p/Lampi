
import unicornhat as unicorn
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("-c", "--colour", required=False, help="Colour of Lamp")
arg.add_argument("-i", "--intensity", required=False, help="Brightness of lamp")
args = vars(arg.parse_args())

def setLED(x,y, background_colour):
    unicorn.set_pixel(x, y, background_colour[0], background_colour[1], background_colour[2])

def runSolid():

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
        for y in range(height):
            for x in range(width):
                setLED(x, y, colour)

        unicorn.show()

if __name__ == "__main__":
    runSolid()

