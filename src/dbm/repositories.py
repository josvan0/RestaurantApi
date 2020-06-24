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
        list = []
        for row in cursor.fetchall():
            list.append(Category(
                id=int(row[0]),
                name=row[1]
            ))
        return list
