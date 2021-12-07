"""
    on_banner
"""
from subprocess import Popen

from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError

from api.common.schema import OnBannerSchema
from api.common.utils import kill


class OnBanner(Resource):
    def post(self):
        kill()
        app.logger.info("onBanner called")
        try:
            schema = OnBannerSchema()
        except ValidationError as err:
            app.logger.error(err)
            return err.messages

        result = schema.loads(request.data.decode('UTF-8'))
        colour_one = ', '.join(map(str, result['colours']['firstColour']))
        colour_two = ', '.join(map(str, result['colours']['secondColour']))

        app.logger.info(result['colours'])
        app.logger.info(result['intensity'])

        Popen(
            [
                'python',
                'banner.py',
                '-i',
                str(result['intensity']),
                '-bc',
                colour_one,
                '-wc',
                colour_two
            ],
            cwd='/home/pi/server/api/tracks/'
        )
        return 'on'
