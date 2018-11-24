#! /usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask,abort,redirect,url_for,render_template,request
import time
import datetime

app = Flask(__name__)

storage_dict = {}

@app.route('/')
def index():
    return render_template('index.html', storage_dict=storage_dict)

@app.route('/add', methods=['GET','POST'])
def add():
    form = request.form
    results = []
    now = datetime.datetime.now()
    timestamp = (str(now.year) + '-' + str(now.month) + '-'
        + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute) 
        + ':' + str(now.second) + '.' + str(now.microsecond))
    if request.method == "POST":
        user_name = form['user_name']
        user_content = form['user_content']
    if user_name and user_content:
        results.append(user_name)
        results.append(user_content)
        storage_dict[timestamp] = results
    return render_template('index.html',storage_dict=storage_dict)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')