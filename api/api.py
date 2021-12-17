"""
    api
"""
import logging
from flask import Flask
from flask_restful import Api
from api.resources.on import On
from api.resources.on_track import OnTrack
from api.resources.off import Off
from api.resources.presets import Presets
from api.resources.get_status import GetStatus, GetStatusWithArgs


app = Flask(__name__)
api = Api(app)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)

api.add_resource(On, '/on')
api.add_resource(Off, '/off')

api.add_resource(OnTrack, '/onSolid', endpoint='onSolid')
api.add_resource(OnTrack, '/onBanner', endpoint='onBanner')
api.add_resource(OnTrack, '/onPulse', endpoint='onPulse')
#onDancer
#onPrancer
api.add_resource(GetStatus, '/getStatus')
api.add_resource(GetStatusWithArgs, '/getStatusWithArgs')
api.add_resource(Presets, '/getPresets')

if __name__ == '__main__':
    app.run(debug=True)
