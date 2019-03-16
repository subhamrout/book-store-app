# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:01:07 2019

@author: Subham Rout
"""

from app import app
from db import db,login_manager

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_first_request
def create_all():
    db.create_all()