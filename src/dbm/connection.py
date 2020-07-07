#!./venv/bin/python
# -*- coding: utf-8 -*-

import pymysql

from .utilities import get_config_section


mysql_data = get_config_section(section='MYSQL_DATA')


# decorator
def connect_db(f):
    def query(**kwargs):
        connection = pymysql.connect(
            host=mysql_data['host'],
            user=mysql_data['user'],
            passwd=mysql_data['password'],
            db=mysql_data['database'],
            autocommit=True
        )

        try:
            with connection.cursor() as cursor:
                return f(cursor, **kwargs)
        except pymysql.Error as e:
            print(f'PyMySQL ERROR [{e.args[0]}]: {e.args[1]}')
        finally:
            connection.close()
    return query
