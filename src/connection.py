#!./venv/bin/python
# -*- coding: utf-8 -*-

import pymysql
from configparser import SafeConfigParser


# read configuration file
CONFIG_SECTION = 'MYSQL_DATA'
config = SafeConfigParser()
config.read('config.ini')

if not config.has_section(CONFIG_SECTION):
    exit(1)

mysql_data = {}
for item in config.items(CONFIG_SECTION):
    mysql_data[item[0]] = item[1]

# free memory
del(config)

# decorator
def connect_db(f):
    def query():
        conn = None
        cur = None

        try:
            conn = pymysql.connect(
                host=mysql_data['host'],
                user=mysql_data['user'],
                passwd=mysql_data['password'],
                db=mysql_data['database']
            )
            cur = conn.cursor()
            return f(cursor=cur)

        except pymysql.Error as e:
            print(f'PyMySQL ERROR [{e.args[0]}]: {e.args[1]}')

        finally:
            print('cerrar')
            if cur:
                cur.close()
            if conn:
                conn.close()

    return query
