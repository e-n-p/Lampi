"""
    on_solid
"""
from subprocess import Popen

from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError

from api.common.schema import OnBasicSchema
from api.common.utils import kill


class OnSolid(Resource):
    def post(self):
        kill()
        app.logger.info("onSolid called")
        try:
            schema = OnBasicSchema()
        except ValidationError as err:
            app.logger.error(err)
            return err.messages
        result = 'on'
        parameters = schema.loads(request.data.decode())
        app.logger.info(parameters)

        colour = ', '.join(map(str, parameters['colour']))

        try:
            Popen(
                [
                    'python',
                    'solid.py',
                    '-i',
                    str(parameters['intensity']),
                    '-c',
                    colour
                ],
                cwd='/home/pi/server/api/tracks/'
            )
        except:
            result = 'failure calling solid'

        return result
