from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/hello_world'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable track warnings
db = SQLAlchemy(app)

from app import routes, models
