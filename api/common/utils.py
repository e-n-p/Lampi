"""
    utils
"""
import re

import psutil
import unicornhat as unicorn

from flask import current_app as app


# only use after killing processes
def clean_up():
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(0.0)
    width,height=unicorn.get_shape()

    for y_coord in range(height):
        for x_coord in range(width):
            unicorn.set_pixel(x_coord, y_coord, int(0), int(0), int(0))
    unicorn.show()

def collect_processes(processes):
    old_session = False
    for process in psutil.process_iter():
        for string in process.cmdline():
            if re.search('pulse.py|banner.py|solid.py', string):
                old_session=True
                processes.append(process)

    return old_session, processes

def kill():
    processes = []
    old_session, processes = collect_processes(processes)

    app.logger.info("clearLamp:kill: " + str(old_session) + ", " + str(processes))

    if old_session:
        for process in processes:
            process.terminate()
            process.wait()
            clean_up()


if __name__ == '__main__':
    kill()
    clean_up()
