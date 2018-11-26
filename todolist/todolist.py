#! /usr/bin/env python
# -*- coding: utf8 -*-

from flask import Flask,abort,redirect,url_for,render_template,request,flash
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#加入这个才能使用flask功能
app.secret_key = 'to_do_list'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./task.db'
# 设置是否在每次连接结束后自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 如果设置成True,SQLAlchemy将会记录所有发到标准输出的（stderr)的语句
# 这对调试很有帮助，默认为false
app.config['SQLALCHEMY_ECHO'] = True
# 如果设置成True (默认情况)，Flask-SQLAlchemy将会追踪对象的修改并且发送信号
# 这需要额外的内存，如果不必要的可以禁用它
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建一个SQLAlchemy实例
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.INTEGER,primary_key = True)
    # 加上这个unique=True会报错，需要确认原因
    # name = db.Column(db.String(64),unique=True)
    name = db.Column(db.String(64))
    create_time = db.Column(db.DateTime,default=datetime.datetime.now())

@app.route('/index')
@app.route('/')
def index():
    # 获取GET方式的参数page，1为默认值
    page = request.args.get('page',1,type=int)
    # 分页，注意这里是paginate,不是pagination,page是当前页，per_page是每页的条数
    pagination = Task.query.order_by(Task.create_time.desc()).paginate(\
        page,per_page=5,error_out=False)
    return render_template('index.html',results=pagination.items,pagination=pagination)

@app.route('/add',methods=['POST','GET'])
def add():
    form = request.form
    task_name = ''
    if request.method == "POST":
        # 获取参数的值，POST使用request.form,GET使用request.args
        task_name = form['task_name']
        print(task_name)
        if task_name:
            insert_database(task_name)
            flash('创建任务成功')
        storage_dict = search_all_database()
    return redirect(url_for('index'))

@app.route('/open_add_todolist_html')
def open_add_todolist_html():
    return render_template('add_todolist.html')

@app.route('/open_modify_todolist_html')
def open_modify_todolist_html():
    ID = request.args.get('ID',1,type=int)
    task = db.session.query(Task).filter(Task.id == ID).one()
    return render_template('modify_todolist.html',task=task)

@app.route('/login',methods=["POST","GET"])
def login():
    form = request.form
    if request.method == "POST":
        username = form['username']
        password = form['password']
        if username != 'admin' and password != 'password':
            return redirect(url_for('to_login_page'))
        else:
            return redirect(url_for('index'))
# 获取参数
@app.route('/modify/<int:ID>',methods=['POST'])
def modify_data(ID):
    form = request.form
    task_name = ''
    if request.method == "POST":
        task_name = form['task_name']
    if len(search_all_database()) > 0:
        # 通过session查询、过滤
        db.session.query(Task).filter(Task.id == ID).update({'name':task_name})
        db.session.commit()
    return redirect(url_for('index'))

def insert_database(name):
    task = Task(name=name)
    db.session.add(task)
    db.session.commit()

def create_datebase():
    try:
        search_all_database()
    except:
        # 根据db.model定义的表和字段创建数据库表
        db.create_all()

def search_all_database():
    return Task.query.all()

@app.route('/search',methods=['POST','GET'])
def search_data_by_keyword():
    form = request.form
    searchword = form['keyword']
    page = request.args.get('page',1,type=int)
    pagination = Task.query.order_by(Task.create_time.desc()).paginate(\
        page,per_page=5,error_out=False)
    if searchword:
        data_list = db.session.query(Task).filter(Task.name.like('%'+searchword+'%')).all()
    return render_template('index.html',results=data_list,pagination=pagination)

@app.route('/delete/<int:ID>')
def delete(ID):
    if len(search_all_database()) > 0:
        db.session.query(Task).filter(Task.id==ID).delete()
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/to_login_page',methods=['POST','GET'])
def to_login_page():
    return render_template('login.html')

if __name__ == "__main__":
    create_datebase()
    app.run(debug=True,host='0.0.0.0')