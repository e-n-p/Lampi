##
# endpoints.py 8/2/2021
##

import lampSwitch
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
        schema = onBannerSchema()
        result = schema.loads(request.data.decode('UTF-8'))

        print(result['colour'])
        print(result['intensity'])

        #Popen(['python', 'banner.py'], cwd='/home/pi/server/tracks/')
        return {'Lamp': 'on but specific'}

class onPulse(Resource):
    def post(self):
        schema = onPulseSchema()
        result = schema.loads(request.data.decode('UTF-8'))
        colours = ', '.join(map(str, result['colour']))

        print(colours)
        print(result['intensity'])

        Popen(['python', 'pulse.py', '-i', str(result['intensity']), '-c', colours], cwd='/home/pi/server/tracks/')
        return {'Lamp': 'on but specific'}


class LampOff(Resource):
    def get(self):
        return kill()

class LampPresets(Resource):
    def get(self):
        return {
                'Lamp0': 'preset1',
                'Lamp1': 'preset2',
            }
