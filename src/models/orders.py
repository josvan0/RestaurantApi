#!./venv/bin/python
# -*- coding: utf-8 -*-

class Orders:
    def __init__(self, id=0, client_id=0):
        self.id = id
        self.client_id = client_id

    # ********** getters **********

    @property
    def id(self):
        return self._id

    @property
    def client_id(self):
        return self._client_id

    # ********** setters **********

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'Excepted [int] in Orders->id. Value: {value}')
        self._id = value

    @property.setter
    def client_id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Orders->client_id. Value: {value}')
        self._client_id = value
