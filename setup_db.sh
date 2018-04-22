#!/bin/bash

# create database
mysql -uroot -e "CREATE DATABASE simple_site" 

# create table
python -c "from app import db; db.create_all()"

# add seeds
python -c "\
from app import db
from app.models.kitten import Kitten

db.session.add(Kitten(name='kitten_0', url='https://i.imgur.com/jajWPT0.jpg'))
db.session.add(Kitten(name='kitten_1', url='http://en.bcdn.biz/Images/2016/8/17/686e3772-a3df-42bf-b5a2-c1f68ad2c66e.jpg'))
db.session.add(Kitten(name='kitten_2', url='https://i.pinimg.com/originals/1d/f7/06/1df706ae30095ad907b9046cdaae2db6.jpg'))
db.session.commit()
"
