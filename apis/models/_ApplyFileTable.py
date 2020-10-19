#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from apis.templates import db


class ApplyFile(db.Model):
    sid = db.Column('sid', db.Integer, primary_key=True)
    extension = db.Column('extension', db.String(15), nullable=False)
    hash = db.Column('hash', db.String(128), nullable=False)
    path = db.Column('path', db.String(100), nullable=False)
    create_timestamp = db.Column('create_timestamp', db.DateTime, nullable=True)
    update_timestamp = db.Column('update_timestamp', db.DateTime, nullable=True)
    status = db.Column('status', db.Integer, nullable=False, default=1)
    # Set foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.sid'), nullable=False)
    # File content
    upload_file_name = db.Column('name', db.String(50), nullable=False)
    upload_file_binary = db.Column('binary', db.LargeBinary, nullable=False)
