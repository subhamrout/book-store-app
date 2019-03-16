# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:35:48 2019

@author: Subham Rout
"""

from db import db
import sqlite3

class BagModel(db.Model):
    __tablename__='bags'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    genre= db.Column(db.String(40))
    price = db.Column(db.Float(precision=2))
   
    
    def __init__(self,name,genre,price):
        self.name = name
        self.genre = genre
        self.price = price
 
        
        
    def json(self):
        return {'book_name':self.name,
                'genre':self.genre,
                'price':self.price,}
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_name(cls,book_name):
        return cls.query.filter_by(name = book_name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    @classmethod    
    def delete_all(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM bags"
        cursor.execute(query)
        connection.commit()
        connection.close()
        