#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

from dbm.repositories import *


class Categories(Resource):
    def get(self):
        category_list = CategoryRepository.get_all_categories()
        return jsonify([ category.json() for category in category_list ])
