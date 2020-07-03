#!./venv/bin/python
# -*- coding: utf-8 -*-

import pymysql

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
