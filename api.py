##
# api.py 8/2/2021
##

from flask import Flask
from flask_restful import Resource, Api
from endpoints import LampOn, onBanner, onPulse, LampOff, LampPresets

app = Flask(__name__)
api = Api(app)


api.add_resource(LampOn, '/on')
api.add_resource(LampOff, '/off')

api.add_resource(onBanner, '/onBanner')
api.add_resource(onPulse, '/onPulse')
#onDancer
#onPrancer

api.add_resource(LampPresets, '/getPresets')

if __name__ == '__main__':
    app.run(debug=True)