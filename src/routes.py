#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import (
    jsonify,
    make_response,
    render_template,
    request
)

from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from dbm.utilities import get_config_section
from dbm.repositories import *


# --------------- init ---------------

auth = HTTPBasicAuth()
server_config = get_config_section(section='SERVER_CONFIG')
APPNAME = server_config['appname']
PORT = server_config['port']
VERSION = server_config['api_version']
del(server_config)


# --------------- middlewares ---------------

@auth.verify_password
def verify_password(username, password):
    user_pass = ClientRepository.get_password_by_username(username=username)
    return check_password_hash(user_pass, password)


# --------------- resources ---------------

class Documentation(Resource):
    def get(self):
        return make_response(
            render_template(
                'index.html',
                appname=APPNAME,
                port=PORT,
                version=VERSION
                ),
            200,
            { 'Content-Type': 'text/html' }
        )


class Categories(Resource):
    def get(self):
        category_list = CategoryRepository.get_all_categories()
        return jsonify([ category.json() for category in category_list ])


class Products(Resource):
    def get(self):
        category_id = request.args.get('categoryId')
        product_list = ProductRepository.get_products_by_category_id(category_id=category_id)
        return jsonify([ product.json() for product in product_list ])
