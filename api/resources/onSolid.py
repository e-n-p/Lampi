
from api.common.schema import onBasicSchema
from api.interfaces.clearLamp import kill
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from subprocess import Popen


class OnSolid(Resource):
    def post(self):
        kill()
        try:
            schema = onBasicSchema()
        except ValidationError as err:
            print(err.messages)
            return err.messages

        result = schema.loads(request.data.decode('UTF-8'))
        colour = ', '.join(map(str, result['colour']))

        print(colour)
        print(result['intensity'])

        Popen(['python', 'solid.py', '-i', str(result['intensity']), '-c', colour], cwd='/home/pi/server/api/tracks/')
        return 'on'
