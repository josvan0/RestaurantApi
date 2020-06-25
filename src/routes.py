#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, make_response, render_template
from flask_restful import Resource

from dbm.utilities import get_config_section
from dbm.repositories import *


server_config = get_config_section(section='SERVER_CONFIG')
APPNAME = server_config['appname']
PORT = server_config['port']
VERSION = server_config['api_version']
del(server_config)


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
