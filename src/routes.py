#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import (
    jsonify,
    request,
    send_file
)

from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from werkzeug.security import check_password_hash

from dbm.utilities import get_config_section
from dbm.repositories import *
from dbm.models import Client


# --------------- init ---------------

auth = HTTPBasicAuth()

# --------------- middlewares ---------------

@auth.verify_password
def verify_password(username, password):
    user_pass = ClientRepository.get_password_by_username(username=username)
    return check_password_hash(user_pass, password)

# --------------- resources ---------------

class Categories(Resource):
    def get(self):
        category_list = CategoryRepository.get_all_categories()
        return jsonify([ category.json() for category in category_list ])


class Clients(Resource):
    @auth.login_required
    def get(self, clientId):
        client = ClientRepository.get_client_by_id(id=clientId)
        return client.json()

    def post(self, clientId=None):
        try:
            client = Client(
                name=request.json.get('name'),
                phone=request.json.get('phone'),
                username=request.json.get('username')
            )
        except ValueError as ex:
            return { 'message': str(ex) }
    
    def put(self, clientId):
        return {}
            

class Images(Resource):
    def get(self, imageId):
        image_path = ProductImageRepository.get_product_image_path_by_id(id=imageId)
        return send_file(
                image_path,
                mimetype='image/jpg'
            ) if image_path else { 'message': 'Image not found' }


class Products(Resource):
    def get(self):
        category_id = request.args.get('categoryId')
        product_list = ProductRepository.get_products_by_category_id(category_id=category_id)
        return jsonify([ product.json() for product in product_list ])


class ProductImages(Resource):
    def get(self, productId):
        return jsonify(ProductImageRepository.get_product_image_ids_by_product_id(product_id=productId))
