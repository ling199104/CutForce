#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# from os.environ import (keys, get)
# print(keys())
# print(get('FLASK_SETTINGS'))
app.config.from_object('setting')

db = SQLAlchemy(app)

# The following lines need to be under the declaration of db
from apis.models import (_UserTable, _ApplyFileTable, _TokenTable)
db.create_all()
