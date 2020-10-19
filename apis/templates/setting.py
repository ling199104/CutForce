#!/usr/bin/env python3
# _*_ coding: utf-8 _*__ * _


from jwt import encode
DEBUG = True

# session 必须要设置key
SECRET_KEY = encode({'Cut-Force': 'KOL-Power-GG'}, 'secret', algorithm='HS256')

DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8"\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
