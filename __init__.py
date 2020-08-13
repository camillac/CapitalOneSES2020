#! /usr/bin/python3

from flask import Flask,render_template,request
import requests
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'coses'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'

db = SQLAlchemy(app)
api_key = 'dceced5acb16100198959ed0cfa3d62b'


@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
