#! /usr/bin/python3

from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)
app.secret_key = 'coses'

# client_id = 'XHm5ttlMqrgKLihC4Si0sw'
api_key = 'dceced5acb16100198959ed0cfa3d62b'
# headers = {'Authorization': 'Bearer %s' % api_key}


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
