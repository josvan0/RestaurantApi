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
    
    @staticmethod
    @connect_db
    def create_client(cursor=None, client=None):
        cursor.execute("""INSERT INTO Client (name, phone, username, password)
                       VALUES (%s, %s, %s, %s)""", (
                           client.name,
                           client.phone,
                           client.username,
                           client.password,
                       ))
        return cursor.lastrowid
    
    @staticmethod
    @connect_db
    def update_client(cursor=None, client=None):
        cursor.execute("""UPDATE Client SET name = %s, phone = %s
                       WHERE id = %s""", (client.name, client.phone, client.id,))
    
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
                       WHERE confirmed = 1 AND paid = 0
                       AND clientId = %s""", (client_id,))
        return [
            Orders(
                id=int(row[0]),
                total=float(row[1])
            )
            for row in cursor.fetchall()
        ]
    
    @staticmethod
    @connect_db
    def get_detail_order_by_id(cursor=None, order_id=None):
        cursor.execute("""SELECT p.Id, p.name, p.description, p.price, op.quantity
                       FROM Order_Product AS op
                       INNER JOIN Product AS p
                       ON op.productId = p.Id
                       WHERE op.orderId = %s""", (order_id,))
        return [
            Order_Product(
                quantity=int(row[4]),
                product=Product(
                    id=int(row[0]),
                    name=row[1],
                    description=row[2],
                    price=float(row[3])
                )
            )
            for row in cursor.fetchall()
        ]

    @staticmethod
    @connect_db
    def get_active_order_by_client_id(cursor=None, client_id=None):
        cursor.execute("""SELECT id, total FROM Orders
                       WHERE confirmed = 0 AND paid = 0
                       AND clientId = %s""", (client_id,))
        row = cursor.fetchone()
        return Orders(
            id=int(row[0]),
            total=float(row[1])
        ) if row else Orders()
    
    @staticmethod
    @connect_db
    def create_order(cursor=None, order=None):
        cursor.execute("""INSERT INTO Orders (clientId, total, confirmed, paid)
                       VALUES (%s, %s, %s, %s)""",(
                           order.client_id,
                           order.total,
                           order.confirmed,
                           order.paid,
                       ))
        return cursor.lastrowid

    @staticmethod
    @connect_db
    def update_total_order(cursor=None, order=None):
        cursor.execute("""UPDATE Orders SET total = %s
                       WHERE id = %s""", (order.total, order.id,))

    @staticmethod
    @connect_db
    def confirm_order(cursor=None, order_id=None):
        cursor.execute("""UPDATE Orders SET confirmed = 1
                       WHERE id = %s""", (order_id,))

    @staticmethod
    @connect_db
    def pay_order(cursor=None, order_id=None):
        cursor.execute("""UPDATE Orders SET paid = 1
                       WHERE id = %s""", (order_id,))


class OrderProductRepository:
    @staticmethod
    @connect_db
    def create_order_product(cursor=None, order_product=None):
        cursor.execute("""INSERT INTO Order_Product (orderId, productId, quantity)
                       VALUES (%s, %s, %s)""", (
                           order_product.order_id,
                           order_product.product_id,
                           order_product.quantity,
                       ))
        return cursor.lastrowid
    
    @staticmethod
    @connect_db
    def get_order_product_id(cursor=None, order_product=None):
        cursor.execute("""SELECT id FROM Order_Product
                       WHERE orderId = %s AND productId = %s""",
                       (order_product.order_id,
                        order_product.product_id,))
        row = cursor.fetchone()
        return int(row[0]) if row else 0

    @staticmethod
    @connect_db
    def update_product_quantity(cursor=None, order_product=None):
        cursor.execute("""UPDATE Order_Product SET quantity = %s
                       WHERE orderId = %s AND productId = %s""",
                       (order_product.quantity,
                        order_product.order_id,
                        order_product.product_id,))

    @staticmethod
    @connect_db
    def delete_order_product_by_id(cursor=None, order_product_id=None):
        cursor.execute("""DELETE FROM Order_Product
                       WHERE id = %s""", (order_product_id,))


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


class SaleRepository:
    @staticmethod
    @connect_db
    def create_sale(cursor=None, sale=None):
        cursor.execute("""INSERT INTO Sale (orderId, paymentMethod)
                       VALUES (%s, %s)""", (
                           sale.order_id,
                           sale.payment_method,
                       ))
        return cursor.lastrowid
