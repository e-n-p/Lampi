
from api.common.schema import onBannerSchema
from api.interfaces.clearLamp import kill
from flask import request, current_app as app
from flask_restful import Resource
from marshmallow import ValidationError
from subprocess import Popen


class OnBanner(Resource):
    def post(self):
        kill()
        app.logger.info("onBanner called")
        try:
            schema = onBannerSchema()
        except ValidationError as err:
            app.logger.error(err)
            return err.messages
        
        result = schema.loads(request.data.decode('UTF-8'))
        colourOne = ', '.join(map(str, result['colours']['firstColour']))
        colourTwo = ', '.join(map(str, result['colours']['secondColour']))

        app.logger.info(result['colours'])
        app.logger.info(result['intensity'])

        Popen(['python', 'banner.py', '-i', str(result['intensity']), '-bc', colourOne, '-wc', colourTwo], cwd='/home/pi/server/api/tracks/')
        return 'on'
