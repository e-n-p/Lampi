"""
    off
"""
from flask_restful import Resource
from flask import current_app as app

from api.common.utils import kill, clean_up


class Off(Resource):
    def get(self):
        app.logger.info("Off called")
        kill()
        clean_up()
        return "off"
