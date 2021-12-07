"""
    on_pulse
"""
from subprocess import Popen

from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError

from api.common.schema import OnBasicSchema
from api.common.utils import kill


class OnPulse(Resource):
    def post(self):
        kill()
        app.logger.info("onPulse called")
        try:
            schema = OnBasicSchema()
        except ValidationError as err:
            app.logger.error(err)
            return err.messages

        result = schema.loads(request.data.decode('UTF-8'))
        colour = ', '.join(map(str, result['colour']))

        app.logger.info(colour)
        app.logger.info(result['intensity'])

        Popen([
            'python',
            'pulse.py',
            '-i',
            str(result['intensity']),
            '-c',
            colour],
            cwd='/home/pi/server/api/tracks/'
        )
        return 'on'
