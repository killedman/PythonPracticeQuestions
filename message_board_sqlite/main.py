#! /usr/bin/env python
# -*- coding:utf8 -*-

from flask import Flask,abort,redirect,url_for,render_template,request
import sqlite3
from datetime import datetime
import time

app = Flask(__name__)
storage_dict = []


def create_database():
    conn = sqlite3.connect('test.db')
    print('opened database sucessfully')
    c = conn.cursor()
    try:
        search_database()
    except:
        c.execute('create table user(ID integer primary key,\
        user_name text not null,user_content text not null,\
        timestamp text not null);')
    c.close()
    conn.commit()
    conn.close()


def insert_database(name,content,times):
    conn = sqlite3.connect('test.db')
    print('opened database sucessfully')
    c = conn.cursor()
    # 此处字符串占位符需要加引号
    c.execute("insert into user(user_name,user_content,timestamp) values ('%s', '%s', '%s')" \
    %(name,content,times))
    c.close()
    conn.commit()
    conn.close()

def search_all_data():
    data_list = []
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("select * from user")
    data_list = cursor.fetchall()
    c.close()
    conn.close()
    return data_list

def search_database():
    data_list = []
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("select user_name,user_content,timestamp from user order by id desc")
    data_list = cursor.fetchall()
    c.close()
    conn.close()
    return data_list

def delete_all_data():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("delete from user")
    c.close()
    conn.commit()
    conn.close()
    
@app.route('/')
def index():
    storage_dict = search_database()
    return render_template('index.html',results=storage_dict)

@app.route('/add',methods = ["POST","GET"])
def add():
    form = request.form
    user_name = ''
    user_content = ''
    now = datetime.now()
    timestamp = str(now.year) + '-' + str(now.month) + '-'\
    + str(now.day) + ' ' + str(now.hour) + ':' + str(now.minute)\
    + ':' + str(now.second) + '.' + str(now.microsecond)
    if request.method == "POST":
        user_name = form['user_name']
        user_content = form['user_content']
        if user_name and user_content:
            insert_database(user_name,user_content,timestamp)
        storage_dict = search_database()
    return render_template('index.html',results=storage_dict)

if __name__ == "__main__":
    create_database()
    print(storage_dict)
    app.run(debug=True,host='0.0.0.0')