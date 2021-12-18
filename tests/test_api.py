"""
    test_api
"""

import unittest
from flask_restful import Api
from flask import Flask

class TestApi(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        self.api = Api(app)

    def tearDown(self):
        self.api = None

    def test_api(self):
        assert self.api is not None


if __name__ == '__main__':
    unittest.main()
