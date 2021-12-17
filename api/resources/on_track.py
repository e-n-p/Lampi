"""
    on_track
"""
from subprocess import Popen

from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError

from api.common.schema import OnDoubleSchema, OnBasicSchema
from api.common.utils import kill


class OnTrack(Resource):
    def post(self):
        kill()
        endpoint = request.endpoint
        app.logger.info("onTrack called with " + endpoint)
        try:
            if endpoint == 'onBanner':
                schema = OnDoubleSchema()
            else:
                schema = OnBasicSchema()
            parameters = schema.loads(request.data.decode('UTF-8'))
        except ValidationError as err:
            app.logger.error(err)
            return err.messages
        result = 'on'
        app.logger.info(parameters)

        if endpoint == 'onBanner':
            call_args = [
                'python',
                'banner.py',
                '-i',
                str(parameters['intensity']),
                '-bc',
                ', '.join(map(str, parameters['colours']['firstColour'])),
                '-wc',
                ', '.join(map(str, parameters['colours']['secondColour']))
            ]
        else:
            call_args = [
                'python',
                'pulse.py' if endpoint == 'onPulse' else 'solid.py',
                '-i',
                str(parameters['intensity']),
                '-c',
                ', '.join(map(str, parameters['colour'])),
            ]

        try:
            Popen(call_args, cwd='/home/pi/server/api/tracks/')
        except:
            result = 'failure calling ' + endpoint

        return result
