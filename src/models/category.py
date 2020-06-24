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

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Category->id. Value: {value}')
        self._id = value

    @property.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Category->name. Value: {value}')
        self._name = value
