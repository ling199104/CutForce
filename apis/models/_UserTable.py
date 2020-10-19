#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from apis.templates import db


class User(db.Model):
    __tablename__ = 'user'
    sid = db.Column('sid', db.Integer, primary_key=True)
    email = db.Column('email', db.String(128), unique=True, nullable=False)
    password = db.Column('password', db.String(128), nullable=False)
    hash = db.Column('hash', db.String(128), unique=True, nullable=False)
    create_timestamp = db.Column('create_timestamp', db.DateTime, nullable=True)
    update_timestamp = db.Column('update_timestamp', db.DateTime, nullable=True)
    status = db.Column(db.Integer, nullable=False, default=1)  # default 1
    roleID = db.Column(db.Integer, nullable=False, default=0)  # 0: normal / 1: admin
    taxID = db.Column(db.String(20), nullable=True)
    # Set relationship
    files = db.relationship('Apply_R_File', backref='user', lazy=True)
    token = db.relationship('Token', backref='user', lazy=True)

    def __repr__(self):
        return '<Post %s>' % self.sid
