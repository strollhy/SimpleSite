from app import app
from app.models.kitten import Kitten
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'

@app.route('/kittens')
def kittens():
    return render_template('kittens.html', kittens=Kitten.query.all())
