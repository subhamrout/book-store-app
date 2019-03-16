# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 21:14:22 2019

@author: Subham Rout
"""

from flask import Flask,render_template,url_for,redirect,flash,request,abort
from form import AddBag,RemoveBag,FormGenre,LoginForm,RegistrationForm
from models.bag import BagModel
from flask_login import login_user,login_required,logout_user
from models.book import BookModel
import sqlite3
from models.user import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'qwerty'
total = 0

  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form  = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Sucessfully')
            next = request.args.get('next')
            
            if next == None or not next[0] == '/':
                next = url_for('books')
            
            return redirect(next)
        else:
            flash('Invalid Credentials!')
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username = form.username.data,
                    password=form.password.data)
        user.save_to_db()
        flash('Thanks for registration!')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out')
    return redirect(url_for('index'))



@app.route('/add-bag',methods=['GET','POST'])
@login_required 
def add_bag():
    global total
    form = AddBag()
    if form.validate_on_submit():
        name = form.name.data
        book = BookModel.find_by_name(name)
        if book:
            bag = BagModel(book.name,book.genre,book.price)        
            bag.save_to_db()
            total += book.price
            flash('The book {} added to the bag'.format(name))        
            return redirect(url_for('add_bag'))
        else:
            flash('The requested book is either invalid or not avaliable in the store currently!')
            return redirect(url_for('add_bag'))
    return render_template('addBag.html',form = form)

@app.route('/remove-bag',methods=['GET','POST'])
@login_required
def remove_bag():
    global total
    form = RemoveBag()
    if form.validate_on_submit():
        name = form.name.data
        bag = BagModel.find_by_name(name)
        if bag:
            total -= bag.price
            bag.delete_from_db()
            flash('The book {} sucessfully removed'.format(name))
            return redirect(url_for('remove_bag'))
        else:
            flash('The book is not avaliable in the bag to be removed!')
            return redirect(url_for('remove_bag'))
    return render_template('removeBag.html',form=form)

@app.route('/bags',methods=['GET','POST'])
@login_required
def bags():
    data = [book.json() for book in BagModel.find_all()]
    return render_template('bags.html',data = data,total=total)

@app.route('/bill',methods=['GET','POST'])
def bill():
    global total
    data = [book.json() for book in BagModel.find_all()]
    tot = total
    total = 0
    BagModel.delete_all()
    return render_template('bill.html',data=data,total = tot)

@app.route('/books',methods=['GET','POST'])
@login_required
def books():
    data = [book.json() for book in BookModel.find_all()]
    return render_template('book.html',data=data)

@app.route('/genre',methods=['GET','POST'])
@login_required
def bookGenre():
    form = FormGenre()
    if form.validate_on_submit():
        genre = form.genre.data
        books = BookModel.find_all_genre(genre)
        book = [b.json() for b in books]
        return render_template('bookGenre.html',book=book)
    return render_template('bGenre.html',form=form)

               
  
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    
