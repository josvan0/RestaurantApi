#!./venv/bin/python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
import pymysql


# read configuration file
CONFIG_SECTION = 'MYSQL_DATA'
config = ConfigParser()
config.read('config.ini')

if not config.has_section(CONFIG_SECTION):
    exit(1)

mysql_data = {}
for item in config.items(CONFIG_SECTION):
    mysql_data[item[0]] = item[1]

# free memory
del(config)
del(CONFIG_SECTION)


# decorator
def connect_db(f):
    def query():
        connection = pymysql.connect(
            host=mysql_data['host'],
            user=mysql_data['user'],
            passwd=mysql_data['password'],
            db=mysql_data['database']
        )

        try:
            with connection.cursor() as cursor:
                return f(cursor)
        except pymysql.Error as e:
            print(f'PyMySQL ERROR [{e.args[0]}]: {e.args[1]}')
        finally:
            connection.close()
    return query
