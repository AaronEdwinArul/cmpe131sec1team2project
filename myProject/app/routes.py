from app import myapp_obj
from flask import render_template, redirect, flash, url_for, request
from app.forms import LoginForm

database={'michael':'123','brandon':'123','aaron':'123','vincent':'123'}

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    username=request.form['username']
    password=request.form['password']
    print(request.form)
    request.form.viewkeys()
    if current_form.username.data == "" or current_form.password.data == "":
        return render_template('login.html',info='Empty Input')
    if username not in database:
        return render_template('login.html',info='Invalid User')
    if database[username]==password:
        return render_template('home.html', name=username, form=current_form)
    else:
        return render_template('login.html',info='Invalid Password')

@myapp_obj.route('/')
def home():
    return render_template('login.html')
