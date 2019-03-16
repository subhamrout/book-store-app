# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:19:51 2019

@author: Subham Rout
"""
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS books (id Integer PRIMARY KEY, name text,genre text, price real)"
cursor.execute(create_table)
connection.commit()

data = [('Midnight Riot','Fantasy',34.45),('Playdate','Fiction',43.3),
        ('Panorama','Historical',12.45),('The Book of Tomorrow','Fiction',35.67),
        ('The Perfect Mistress','Romance',23.45),('Home for a Spell','Fiction',23.56)]

query = "INSERT INTO books VALUES(NULL,?,?,?)"

    

cursor.executemany(query,data)
q = "SELECT * FROM books"
for row in cursor.execute(q):
    print(row)


connection.commit()
connection.close()

