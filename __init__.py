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

labels = [
    'Take Out', '(expected)',
    'Groceries', '(expected)',
    'Entertainment', '(expected)',
    'Misc', '(expected)'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA"
]

@app.route('/graphs')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('graphs.html', title='Monthly Expenses', max=17000, labels=bar_labels, values=bar_values)

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
