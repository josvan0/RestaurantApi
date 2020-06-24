#!../venv/bin/python
# -*- coding: utf-8 -*-

class Client:
    def __init__(self, id=0, name='', phone='', username='', password=''):
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

    @property.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(
                f'Excepted [int] in Client->id. Value: {value}')
        self._id = value

    @property.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->name. Value: {value}')
        self._name = value

    @property.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->phone. Value: {value}')
        self._phone = value

    @property.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->username. Value: {value}')
        self._username = value

    @property.setter
    def password(self, value):
        if not isinstance(value, str):
            raise ValueError(
                f'Excepted [str] in Client->password. Value: {value}')
        self._password = value
