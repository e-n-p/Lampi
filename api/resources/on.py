"""
    on
"""
from subprocess import Popen
from flask_restful import Resource
from flask import current_app as app

from api.common.utils import lamp_switch


class On(Resource):
    def get(self):
        app.logger.info("on called")
        result = 'on'
        try:
            Popen(
                [
                    'python',
                    'banner.py',
                    '-i',
                    '1.0',
                    '-bc',
                    '255,0,255',
                    '-wc',
                    '220,20,60'
                ],
                cwd='/home/pi/server/api/tracks/'
            )
        except:
            result = 'failure calling banner'

        app.logger.info(result)
        return result
