# -*- coding:utf-8 -*-

DEBUG = True

DIRLECT = 'mysql'
DERVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_demo'

SECRET_KEY = 'xeUlryB9B7qQCHpA4z/L5YMnMh4B59Ao'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIRLECT, DERVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
