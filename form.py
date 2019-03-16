# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:43:36 2019

@author: Subham Rout
"""
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from models.user import User


class AddBag(FlaskForm):
    name = StringField('Name of Book: ')
    submit = SubmitField('Add Book')
    
    
class RemoveBag(FlaskForm):
    name = StringField('Name of book you want to remove: ')
    submit = SubmitField("Remove Book")
    
class FormGenre(FlaskForm):
    genre = StringField('Name the genre: ')
    submit = SubmitField("Find Book")
   
    
class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Log In')    
    
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been already registered !')
    
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken')
            