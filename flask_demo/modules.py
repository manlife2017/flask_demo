# -*- coding:utf-8 -*-
from exts import db
#
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)


