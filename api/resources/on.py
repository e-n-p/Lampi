
from api.interfaces.lampSwitch import lampSwitch
from flask_restful import Resource
from flask import current_app as app


class On(Resource):
    def get(self):
        app.logger.info("on called")
        state = lampSwitch()
        return state
