
import json
from flask_restful import Resource
from flask import current_app as app

class Presets(Resource):
    def get(self):
        app.logger.info("presets called")
        with open('/home/pi/server/api/common/presets.json') as data:
            json_data = json.load(data)

        return json_data
