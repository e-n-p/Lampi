
from api.interfaces.clearLamp import kill, cleanUp
from flask_restful import Resource
from flask import current_app as app


class Off(Resource):
    def get(self):
        app.logger.info("Off called")
        kill()
        cleanUp()
        return "off"

