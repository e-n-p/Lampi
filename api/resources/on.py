"""
    on
"""
from flask_restful import Resource
from flask import current_app as app

from api.common.utils import lamp_switch


class On(Resource):
    def get(self):
        app.logger.info("on called")
        state = lamp_switch()
        app.logger.info(state)
        return state
