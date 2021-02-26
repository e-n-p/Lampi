
import json
from flask_restful import Resource

class Presets(Resource):
    def get(self):

        with open('/home/pi/server/api/common/presets.json') as data:
            json_data = json.load(data)
            print(json_data)

        return json_data
