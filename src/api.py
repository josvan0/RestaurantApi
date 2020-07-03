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

app = Flask(
    server_config['appname'],
    static_url_path=server_config['static_path'], # removes any preceding path from the URL
    static_folder=server_config['static_folder'], # folder for static files
    template_folder=server_config['template_folder'] # folder for templates
)

api = Api(app)
api.add_resource(Documentation, '/', endpoint='home')
api.add_resource(Categories, f'{API_NAMESPACE}/categories', endpoint='categories')
api.add_resource(Products, f'{API_NAMESPACE}/products', endpoint='products')

del(server_config)
del(API_NAMESPACE)


if __name__ == '__main__':
    app.run(port=PORT)
