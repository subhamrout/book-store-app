# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:31:18 2019

@author: Subham Rout
"""
from db import db

class BookModel(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    genre = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self,name,genre,price):
        self.name = name
        self.genre = genre
        self.price = price
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod    
    def find_by_name(cls,book_name):
        return cls.query.filter_by(name=book_name).first()
    
    def json(self):
        return {'name':self.name,
                'genre':self.genre,
                'price':self.price}
    
    @classmethod
    def find_all_genre(cls,genre):
        return cls.query.filter_by(genre=genre)    