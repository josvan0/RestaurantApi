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
        return [ Category(id=int(row[0]), name=row[1]) for row in cursor.fetchall() ]
