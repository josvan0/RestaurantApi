#!./venv/bin/python
# -*- coding: utf-8 -*-

import pymysql

from werkzeug.security import generate_password_hash

from .connection import connect_db
from .models import *


class CategoryRepository:
    @staticmethod
    @connect_db
    def get_all_categories(cursor=None):
        cursor.execute('SELECT * FROM Category')
        return [
            Category(
                id=int(row[0]),
                name=row[1]
            )
            for row in cursor.fetchall()
        ]


class ClientRepository:
    @staticmethod
    @connect_db
    def get_password_by_username(cursor=None, username=None):
        cursor.execute("""SELECT password FROM Client
                       WHERE username = %s""", (username,))
        row = cursor.fetchone()
        return row[0] if row else ''
    
    @staticmethod
    @connect_db
    def create_client(cursor=None, client=None):
        cursor.execute("""INSERT INTO Client (name, phone, username, password)
                       VALUES (%s, %s, %s, %s)""", (
                           client.name,
                           client.phone,
                           client.username,
                           generate_password_hash(client.password),
                       ))
        return cursor.lastrowid
    
    @staticmethod
    @connect_db
    def update_client(cursor=None, client=None):
        cursor.execute("""UPDATE Client SET name = %s, phone = %s
                       WHERE id = %s""", (client.name, client.phone, client.id,))
        return True
    
    @staticmethod
    @connect_db
    def update_password(cursor=None, client=None):
        cursor.execute("""UPDATE Client SET password = %s
                       WHERE id = %s""", (client.password, client.id,))
        
    @staticmethod
    @connect_db
    def get_client_by_id(cursor=None, id=None):
        cursor.execute("""SELECT * FROM Client
                       WHERE id = %s""", (id,))
        row = cursor.fetchone()
        return Client(
            id=int(row[0]),
            name=row[1],
            phone=row[2],
            username=row[3]
        ) if row else Client()


class OrdersRepository:
    @staticmethod
    @connect_db
    def get_orders_confirmed_by_client_id(cursor=None, client_id=None):
        cursor.execute("""SELECT id, total FROM Orders
                       WHERE confirmed = 1 AND clientId = %s""", (client_id,))
        return [
            Orders(
                id=int(row[0]),
                total=float(row[1])
            )
            for row in cursor.fetchall()
        ]


class ProductRepository:
    @staticmethod
    @connect_db
    def get_products_by_category_id(cursor=None, category_id=None):
        if category_id:
            cursor.execute("""SELECT * FROM Product AS p
                           INNER JOIN Category_Product AS cp
                           ON cp.productId = p.Id
                           WHERE cp.categoryId = %s""", (category_id,))
        else:
            cursor.execute('SELECT * FROM Product')
        
        return [
            Product(
                id=int(row[0]),
                name=row[1],
                description=row[2],
                price=float(row[3])
            )
            for row in cursor.fetchall()
        ]


class ProductImageRepository:
    @staticmethod
    @connect_db
    def get_product_image_ids_by_product_id(cursor=None, product_id=None):
        cursor.execute("""SELECT id FROM ProductImage
                       WHERE productId = %s""", (product_id,))
        return [ int(row[0]) for row in cursor.fetchall() ]
    
    @staticmethod
    @connect_db
    def get_product_image_path_by_id(cursor=None, id=None):
        cursor.execute("""SELECT path FROM ProductImage
                       WHERE id = %s""", (id,))
        row = cursor.fetchone()
        return row[0] if row else None
