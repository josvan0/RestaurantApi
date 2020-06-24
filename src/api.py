#!./venv/bin/python
# -*- coding: utf-8 -*-

from configparser import ConfigParser

from flask import Flask
from flask_restful import Api

from routes import *


# ********** declaration **********

CONFIG_SECTION = 'APP_CONFIG'
appname = __name__
server_port = '9000'

config = ConfigParser()
config.read('config.ini')

if config.has_option(CONFIG_SECTION, 'appname'):
    appname = config.get(CONFIG_SECTION, 'appname')
if config.has_option(CONFIG_SECTION, 'server_port'):
    server_port = config.get(CONFIG_SECTION, 'server_port')

app = Flask(appname)

del(config)
del(CONFIG_SECTION)
del(appname)

# ********** server setup **********

api = Api(app)
api.add_resource(Categories, '/categories')

if __name__ == '__main__':
    app.run(port=server_port)
