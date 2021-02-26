
from api.interfaces.clearLamp import kill
from flask import request
from flask_restful import Resource
from api.common.schema import onBannerSchema
from subprocess import Popen

class OnBanner(Resource):
    def post(self):
        kill()
        schema = onBannerSchema()
        result = schema.loads(request.data.decode('UTF-8'))
        colourOne = ', '.join(map(str, result['colours']['firstColour']))
        colourTwo = ', '.join(map(str, result['colours']['secondColour']))

        print(result['colours'])
        print(result['intensity'])

        Popen(['python', 'banner.py', '-i', str(result['intensity']), '-bc', colourOne, '-wc', colourTwo], cwd='/home/pi/server/api/tracks/')
        return 'on'
