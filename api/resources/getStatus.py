from flask import request, current_app as app
import psutil
import re

from flask_restful import Resource

class GetStatusWithArgs(Resource):
    def get(self):
        app.logger.info("getStatus called")
        process_details = []

        for process in psutil.process_iter():
            for string in process.cmdline():
                if re.search('pulse.py|banner.py|solid.py', string):
                    print(process.as_dict()['cmdline'])
                    process_details.append(process.as_dict()['cmdline'][1])
                    process_details.append(process.as_dict()['cmdline'][3])
                    process_details.append(process.as_dict()['cmdline'][5])

                    if process.as_dict()['cmdline'][1] == 'banner.py':
                        process_details.append(process.as_dict()['cmdline'][7])

                    return str(process_details)

        return '0'


class GetStatus(Resource):
    def get(self):
        app.logger.info("getStatus called")

        for process in psutil.process_iter():
            for string in process.cmdline():
                if re.search('pulse.py|banner.py|solid.py', string):
                    return '1'
        return '0'

