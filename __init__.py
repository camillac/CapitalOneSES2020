#! /usr/bin/python3

from flask import Flask,render_template,request
import requests
import json


app = Flask(__name__)
app.secret_key = 'coses'


labels = [
    'Take Out', 'Take Out (expected)',
    'Groceries', 'Groceries (expected)',
    'Entertainment', 'Entertainment (expected)',
    'Misc', 'Misc (expected)'
]

@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/get_goals')
def goals():
    return render_template('goals.html')

@app.route('/set_goals', methods = ["POST"])
def set_goals():
    req = request.form
    print(req)
    # budg = req.get("t1")
    print("==========")
    print("HELLO")
    type(req.get("t1"))
    req.get("t1")
    print("==========")
    budg = int(req.get("t1"))
    print("==========")
    print("==========")
    dining = int(req.get("t2"))
    groceries = int(req.get("t3"))
    ent = int(req.get("t4"))
    misc = int(req.get("t5"))
    SPENT = 400
    values = []
    values.append(SPENT)
    values.append(int(budg * (dining/100)))
    values.append(SPENT)
    values.append(int(budg * (groceries/100)))
    values.append(SPENT)
    values.append(int(budg * (ent/100)))
    values.append(SPENT)
    values.append(int(budg * (misc/100)))
    bar_labels=labels
    maxy = max(values)
    return render_template('graphs.html',title='Monthly Expenses', max=maxy, labels=bar_labels, values=values )

if __name__ == '__main__':
    app.debug = True
    app.run()
