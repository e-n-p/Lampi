
from api.interfaces.clearLamp import kill
from flask_restful import Resource


class Off(Resource):
    def get(self):
        return kill()

