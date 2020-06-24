#!./venv/bin/python
# -*- coding: utf-8 -*-

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

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->id. Value: {value})')
        self._id = value

    @property.setter
    def order_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->order_id. Value: {value})')
        self._order_id = value

    @property.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->product_id. Value: {value})')
        self._product_id = value

    @property.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Order_Product->quantity. Value: {value})')
        self._quantity = value
