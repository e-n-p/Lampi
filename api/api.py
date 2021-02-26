##
# api.py 8/2/2021
##

from flask import Flask
from flask_restful import Resource, Api
from api.resources.on import On
from api.resources.onBanner import OnBanner
from api.resources.onPulse import OnPulse
from api.resources.onSolid import OnSolid
from api.resources.off import Off
from api.resources.presets import Presets


app = Flask(__name__)
api = Api(app)


api.add_resource(On, '/on')
api.add_resource(Off, '/off')

api.add_resource(OnSolid, '/onSolid')
api.add_resource(OnBanner, '/onBanner')
api.add_resource(OnPulse, '/onPulse')
#onDancer
#onPrancer

api.add_resource(Presets, '/getPresets')

if __name__ == '__main__':
    app.run(debug=True)