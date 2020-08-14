#! /usr/bin/python3

from flask import Flask,render_template,request
import requests
import json


app = Flask(__name__)
app.secret_key = 'coses'

api_key = 'dceced5acb16100198959ed0cfa3d62b'

labels = [
    'Take Out', 'Take Out Goal',
    'Groceries', 'Groceries Goal',
    'Entertainment', 'Entertainment Goal',
    'Misc', 'Misc Goal'
]
GOAL = 1500
values = [
    967.67, GOAL, 1190.89, GOAL, 1079.75, GOAL, 1349.19, GOAL
]

colors = [
    "#F7464A", "#FF0000", "#46BFBD", "#FF0000", "#FDB45C", "#FF0000", 
    "#FEDCBA", "#FF0000"
]

@app.route('/graphs')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('graphs.html', title='Monthly Expenses', max=GOAL, labels=bar_labels, values=bar_values)

@app.route('/')
def main():
    return render_template('welcome.html')
@app.route('/get_goal')
def get_goal():
    return render_template('goals.html')
@app.route('/goals')
def goals():
    return render_template('goals.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
