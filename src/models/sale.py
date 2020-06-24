#!./venv/bin/python
# -*- coding: utf-8 -*-

class Sale:
    def __init__(self, id=0, order_id=0, payment_method=0, total=0.0):
        self.id = id
        self.order_id = order_id
        self.payment_method = payment_method
        self.total = total

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

    @property
    def total(self):
        return self._total

    # ********** setters **********

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Sale->id. Value: {value}')
        self._id = value

    @property.setter
    def order_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Sale->order_id. Value: {value}')
        self._order_id = value

    @property.setter
    def payment_method(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Sale->payment_method. Value: {value}')
        self._payment_method = value

    @property.setter
    def total(self, value):
        if not isinstance(value, float):
            raise ValueError(
                f'Excepted [float] in Sale->total. Value: {value}')
        self._total = value
