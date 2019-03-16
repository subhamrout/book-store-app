# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:21:19 2019

@author: Subham Rout
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()