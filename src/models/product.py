#!./venv/bin/python
# -*- coding: utf-8 -*-

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

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Product->id. Value: {value}')
        self._id = value

    @property.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Product->name. Value: {value}')
        self._name = value
        
    @property.setter
    def description(self, value):
        if not isinstance(value, (str, None)):
            raise ValueError(
                f'Excepted [str] in Product->description. Value: {value}')
        self._description = value
        
    @property.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError(
                f'Excepted [float] in Product->price. Value: {value}')
        self._price = value
