
from api.interfaces.clearLamp import kill
from flask import request
from flask_restful import Resource
from api.common.schema import onPulseSchema
from subprocess import Popen


class OnPulse(Resource):
    def post(self):
        kill()
        schema = onPulseSchema()
        result = schema.loads(request.data.decode('UTF-8'))
        colour = ', '.join(map(str, result['colour']))

        print(colour)
        print(result['intensity'])

        Popen(['python', 'pulse.py', '-i', str(result['intensity']), '-c', colour], cwd='/home/pi/server/api/tracks/')
        return 'on'
