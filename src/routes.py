#!./venv/bin/python
# -*- coding: utf-8 -*-

from flask import (
    jsonify,
    request,
    make_response,
    send_file
)

from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

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


# --------------- helpers ---------------

def make_bad_format_response(message):
    return make_response(jsonify({
        'message': message
    }), 422, {
        'Content-Type': 'application/json'
    })


# --------------- resources ---------------

class Categories(Resource):
    def get(self):
        category_list = CategoryRepository.get_all_categories()
        return jsonify([ category.json() for category in category_list ])


class Clients(Resource):
    @auth.login_required
    def get(self, clientId):
        client = ClientRepository.get_client_by_id(id=clientId)
        return jsonify(client.json())

    def post(self, clientId=None):
        try:
            new_client = Client(
                name=request.json.get('name'),
                phone=request.json.get('phone'),
                username=request.json.get('username'),
                password=generate_password_hash(request.json.get('password'))
            )
            
            client_id = ClientRepository.create_client(client=new_client)
            return jsonify({
                'clientId': client_id
            }) if client_id else jsonify({
                'message': f'Username "{new_client.username}" already exists, please choose other username'
            })
        except ValueError as ex:
            return make_bad_format_response(str(ex))
        except TypeError as ex:
            print(ex)
            return make_bad_format_response('Password cannot be empty')
    
    @auth.login_required
    def put(self, clientId):
        try:
            client_to_update = Client(
                id=clientId,
                name=request.json.get('name'),
                phone=request.json.get('phone')
            )
            
            ClientRepository.update_client(client=client_to_update)
            return jsonify({ 'message': 'Client updated successfully' })
        except ValueError as ex:
            return make_bad_format_response(str(ex))
            

class ClientPassword(Resource):
    @auth.login_required
    def put(self, clientId):
        new_password = request.json.get('password')
        if not new_password or new_password == '':
            return make_bad_format_response('Password cannot be empty')
        
        try:
            client_to_update = Client(
                id=clientId,
                password=generate_password_hash(new_password)
            )
            
            ClientRepository.update_password(client=client_to_update)
            return jsonify({ 'message': 'Password updated successfully' })
        except ValueError as ex:
            return make_error_response(str(ex))


class Images(Resource):
    def get(self, imageId):
        image_path = ProductImageRepository.get_product_image_path_by_id(id=imageId)
        return send_file(
                image_path,
                mimetype='image/jpg'
            ) if image_path else jsonify({ 'message': 'Image not found' })


class Products(Resource):
    def get(self):
        category_id = request.args.get('categoryId')
        product_list = ProductRepository.get_products_by_category_id(category_id=category_id)
        return jsonify([ product.json() for product in product_list ])


class ProductImages(Resource):
    def get(self, productId):
        return jsonify(ProductImageRepository.get_product_image_ids_by_product_id(product_id=productId))
