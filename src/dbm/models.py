#!./venv/bin/python
# -*- coding: utf-8 -*-

class Category:
    def __init__(self, id=0, name=''):
        self.id = id
        self.name = name

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Category->id. Value: {value}')
        self._id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Category->name. Value: {value}')
        self._name = value

    def json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Category_Product:
    def __init__(self, category_id=0, product_id=0):
        self.category_id = category_id
        self.product_id = product_id

    # ********** getters **********

    @property
    def category_id(self):
        return self._category_id

    @property
    def product_id(self):
        return self._product_id

    # ********** setters **********

    @category_id.setter
    def category_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Category_Product->category_id. Value: {value}')
        self._category_id = value

    @product_id.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Category_Product->product_id. Value: {value}')
        self._product_id = value


class Client:
    def __init__(self, id=0, name='', phone=None, username='', password=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.username = username
        self.password = password

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Client->id. Value: {value}')
        self._id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->name. Value: {value}')
        self._name = value

    @phone.setter
    def phone(self, value):
        if not value:
            self._phone = None
        elif not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->phone. Value: {value}')
        self._phone = value

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->username. Value: {value}')
        self._username = value

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->password. Value: {value}')
        self._password = value
    
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'username': self.username
        }


class Order_Product:
    def __init__(self, id=0, order_id=0, product_id=0, quantity=0):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def order_id(self):
        return self._order_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def quantity(self):
        return self._quantity

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->id. Value: {value})')
        self._id = value

    @order_id.setter
    def order_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->order_id. Value: {value})')
        self._order_id = value

    @product_id.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->product_id. Value: {value})')
        self._product_id = value

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->quantity. Value: {value})')
        self._quantity = value


class Orders:
    def __init__(self, id=0, client_id=0, total=0.0, confirmed=False):
        self.id = id
        self.client_id = client_id
        self.total = total
        self.confirmed = confirmed

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def client_id(self):
        return self._client_id

    @property
    def total(self):
        return self._total

    @property
    def confirmed(self):
        return self._confirmed

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Orders->id. Value: {value}')
        self._id = value

    @client_id.setter
    def client_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Orders->client_id. Value: {value}')
        self._client_id = value

    @total.setter
    def total(self, value):
        if not isinstance(value, float):
            raise ValueError(
                f'Excepted [float] in Sale->total. Value: {value}')
        self._total = value

    @confirmed.setter
    def confirmed(self, value):
        if not isinstance(value, bool):
            raise ValueError(
                f'Excepted [bool] in Orders->confirmed. Value: {value}')
        self._confirmed = value

    def json(self):
        return {
            'id': self.id,
            'clientId': self.client_id,
            'total': self.total,
            'confirmed': self.confirmed
        }


class Product:
    def __init__(self, id=0, name='', description=None, price=0.0):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def price(self):
        return self._price

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Product->id. Value: {value}')
        self._id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Product->name. Value: {value}')
        self._name = value
        
    @description.setter
    def description(self, value):
        if not value:
            self._description = None
        elif not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Product->description. Value: {value}')
        self._description = value
        
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError(
                f'Excepted [float] in Product->price. Value: {value}')
        self._price = value

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }


class ProductImage:
    def __init__(self, id=0, product_id=0, path=''):
        self.id = id
        self.product_id = product_id
        self.path = path

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def product_id(self):
        return self._product_id

    @property
    def path(self):
        return self._path

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in ProductImage->id. Value: {value}')
        self._id = value

    @product_id.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in ProductImage->product_id. Value: {value}')
        self._product_id = value

    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in ProductImage->path. Value: {value}')
        self._path = value

    def json(self):
        return {
            'id': self.id,
            'productId': self.product_id,
            'path': self.path
        }


class Sale:
    def __init__(self, id=0, order_id=0, payment_method=0):
        self.id = id
        self.order_id = order_id
        self.payment_method = payment_method

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def order_id(self):
        return self._order_id

    @property
    def payment_method(self):
        return self._payment_method

    # ********** setters **********

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Sale->id. Value: {value}')
        self._id = value

    @order_id.setter
    def order_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Sale->order_id. Value: {value}')
        self._order_id = value

    @payment_method.setter
    def payment_method(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Sale->payment_method. Value: {value}')
        self._payment_method = value

    def json(self):
        return {
            'id': self.id,
            'orderId': self.order_id,
            'paymentMethod': self.payment_method
        }
