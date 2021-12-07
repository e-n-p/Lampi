"""
    get_status
"""
import re

from flask import current_app as app
import psutil

from flask_restful import Resource

class GetStatusWithArgs(Resource):
    def get(self):
        app.logger.info("getStatus called")
        process_details = []

        for process in psutil.process_iter():
            for string in process.cmdline():
                if re.search('pulse.py|banner.py|solid.py', string):
                    process_dict = process.as_dict()
                    app.logger.info(str(process_dict['cmdline']))
                    process_details.append(process_dict['cmdline'][1][:-3])
                    process_details.append(process_dict['cmdline'][3])
                    process_details.append(str(process_dict['cmdline'][5]).replace(" ", ""))

                    if process_dict['cmdline'][1] == 'banner.py':
                        process_details[2] += (
                            ';' + str(process.as_dict()['cmdline'][7]).replace(" ", "")
                        )

                    app.logger.info(str(process_details))

        return process_details



class GetStatus(Resource):
    def get(self):
        app.logger.info("getStatus called")

        for process in psutil.process_iter():
            for string in process.cmdline():
                if re.search('pulse.py|banner.py|solid.py', string):
                    return '1'
        return '0'
