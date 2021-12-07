"""
    on_solid
"""
import logging
from subprocess import Popen

from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError

from api.common.schema import OnBasicSchema
from api.common.utils import kill


logger = logging.getLogger(__name__)

class OnSolid(Resource):
    def post(self):
        kill()
        app.logger.info("onSolid called")
        try:
            schema = OnBasicSchema()
            app.logger.info(request.data.decode())
            result = schema.loads(request.data.decode())
        except ValidationError as err:
            app.logger.error(err)
            return err.messages

        colour = ', '.join(map(str, result['colour']))

        app.logger.info(colour)
        app.logger.info(result['intensity'])

        Popen(
            [
                'python',
                'solid.py',
                '-i',
                str(result['intensity']),
                '-c',
                colour
            ],
            cwd='/home/pi/server/api/tracks/'
        )
        return 'on'
