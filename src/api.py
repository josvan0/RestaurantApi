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

# --------------- API routes ---------------

api.add_resource(Categories, f'{API_NAMESPACE}/categories', endpoint='categories')
api.add_resource(
    Clients,
    f'{API_NAMESPACE}/clients',
    f'{API_NAMESPACE}/clients/<int:clientId>',
    endpoint='clients'
)
api.add_resource(ClientPassword, f'{API_NAMESPACE}/clients/<int:clientId>/password', endpoint='password')
api.add_resource(Images, f'{API_NAMESPACE}/images/<int:imageId>', endpoint='images')
api.add_resource(Products, f'{API_NAMESPACE}/products', endpoint='products')
api.add_resource(ProductImages, f'{API_NAMESPACE}/products/<int:productId>/images', endpoint='productImages')

del(server_config)
del(API_NAMESPACE)


if __name__ == '__main__':
    app.run(port=PORT)
