
from api.interfaces.lampSwitch import lampSwitch
from flask_restful import Resource

class On(Resource):
    def get(self):
        state = lampSwitch()
        return state
