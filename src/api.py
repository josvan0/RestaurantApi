#!../venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    app.run(port='9000')
