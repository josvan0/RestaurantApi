#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from dbm.utilities import get_config_section
from routes import *


# --------------- server setup ---------------

server_config = get_config_section(section='SERVER_CONFIG')
API_NAMESPACE = f"/api/v{server_config['api_version']}"
PORT = server_config['port']

app = Flask(server_config['appname'])
api = Api(app)

api.add_resource(Categories, f'{API_NAMESPACE}/categories', endpoint='categories')
api.add_resource(Products, f'{API_NAMESPACE}/products', endpoint='products')

del(server_config)
del(API_NAMESPACE)


if __name__ == '__main__':
    app.run(port=PORT)
