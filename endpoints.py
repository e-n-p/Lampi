##
# endpoints.py 8/2/2021
##

import lampSwitch
import json
from clearLamp import kill
from flask import request
from flask_restful import Resource
from subprocess import Popen
from schema import onBannerSchema, onPulseSchema


class LampOn(Resource):
    def get(self):
        state = lampSwitch.lampSwitch()
        return state


class onBanner(Resource):
    def post(self):
        kill()
        schema = onBannerSchema()
        result = schema.loads(request.data.decode('UTF-8'))
        colourOne = ', '.join(map(str, result['colours']['firstColour']))
        colourTwo = ', '.join(map(str, result['colours']['secondColour']))

        print(result['colours'])
        print(result['intensity'])

        Popen(['python', 'banner.py', '-i', str(result['intensity']), '-bc', colourOne, '-wc', colourTwo], cwd='/home/pi/server/tracks/')
        return 'on'

class onPulse(Resource):
    def post(self):
        kill()
        schema = onPulseSchema()
        result = schema.loads(request.data.decode('UTF-8'))
        colour = ', '.join(map(str, result['colour']))

        print(colour)
        print(result['intensity'])

        Popen(['python', 'pulse.py', '-i', str(result['intensity']), '-c', colour], cwd='/home/pi/server/tracks/')
        return 'on'


class LampOff(Resource):
    def get(self):
        return kill()

class LampPresets(Resource):
    def get(self):

        with open('/home/pi/server/presets.json') as data:
            json_data = json.load(data)
            print(json_data)

        return json_data
