#!./venv/bin/python
# -*- coding: utf-8 -*-

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

    @property.setter
    def category_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Category_Product->category_id. Value: {value}')
        self._category_id = value

    @property.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Category_Product->product_id. Value: {value}')
        self._product_id = value
