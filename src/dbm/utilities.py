#!./venv/bin/python
# -*- coding: utf-8 -*-

from configparser import ConfigParser


def get_config_section(file='config.ini', section=None):
    if not section:
        return {}
    
    parser = ConfigParser()
    parser.read(file)
    
    if not parser.has_section(section):
        return {}
    
    config = {}
    for item in parser.items(section):
        config[item[0]] = item[1]
    return config
