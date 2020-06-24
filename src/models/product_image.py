#!./venv/bin/python
# -*- coding: utf-8 -*-

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

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in ProductImage->id. Value: {value}')
        self._id = value

    @property.setter
    def product_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in ProductImage->product_id. Value: {value}')
        self._product_id = value

    @property.setter
    def path(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in ProductImage->path. Value: {value}')
        self._path = value
