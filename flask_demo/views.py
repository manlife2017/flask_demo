# -*- coding:utf-8 -*-
import hashlib
from flask import Flask,render_template, request, redirect, url_for
from exts import db
import config
from modules import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form.get('name', None)
        user_list = User.query.filter(User.name==name).all()
        if user_list:
            return render_template('register.html', register_info='<div class="alert alert-danger" role="alert">账号已存在</div>')
        else:
            password = request.form.get('password', None)
            password = hashlib.sha1(password).hexdigest()
            user = User(name=name, password=password)
            db.session(user)
            db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()