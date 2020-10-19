#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from apis.templates import db


class Token(db.Model):
    token = db.Column('token', db.String(128), nullable=False)
    ip_address = db.Column('ip_address', db.String(32), nullable=False)
    create_timestamp = db.Column('create_timestamp', db.DateTime, nullable=True)
    update_timestamp = db.Column('update_timestamp', db.DateTime, nullable=True)
    status = db.Column('status', db.Integer, nullable=False, default=1)
    # Set foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.sid'), nullable=False)
