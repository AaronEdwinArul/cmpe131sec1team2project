from app import myapp_obj
from flask import render_template, redirect, flash, request
from app.forms import LoginForm, SignupForm, PostForm, HomePageForm
from app.models import User, Post, Likes, Follows, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app import db

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    errorMessage = ''
    if current_form.validate_on_submit():
        user = User.query.filter_by(username=current_form.username.data).first()
        if user is not None and not check_password_hash(user.password, current_form.password.data):
            errorMessage = 'Invalid username or password'
            print(current_form.password.data)
            print(generate_password_hash(current_form.password.data))
            print(user.password)
            print(check_password_hash(user.password, current_form.password.data))
        else:
            return redirect('/home')
        login_user(user, remember=current_form.remember_me.data)
    return render_template('login.html', form=current_form, errorMessage=errorMessage)

@myapp_obj.route('/logout')
def logout():
    logout_user()
    return render_template('base.html')

@myapp_obj.route('/home', methods=['POST', 'GET'])
def home():
    a = 8
    name = 'Friend'
    current_form = HomePageForm()
    if current_form.validate_on_submit():
       return redirect('/home')
    return render_template('home.html', form=current_form)

@myapp_obj.route('/signup', methods = ['POST','GET'])
def create():
    current_form = SignupForm()
    errorMessage = ''
    if current_form.validate_on_submit():   
        if not(validPassword(current_form.password.data)):
            errorMessage = 'Password must be longer than 8 characters'
        elif not(validEmail(current_form.email.data)):
            errorMessage = 'Invalid email address (must have domain .com,.org,.edu)'
        else:
            user = User()
            user.first = generate_password_hash(current_form.first.data)
            user.last = generate_password_hash(current_form.last.data)
            user.email = generate_password_hash(current_form.email.data)
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')        #redirect to login page when implemented
    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])
#@login_required
def post():
    current_form = PostForm()
    if current_form.validate_on_submit():
        post = Post()
        post.post = current_form.text.data
        post.link = current_form.link.data
        post.user_id = 1
        with myapp_obj.app_context():
            db.session.add(post)
            db.session.commit()
        return redirect('/home')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/')
def base():
    return render_template('base.html')

# helper functions

def check_password_hash(pw_hash, password):
    return pw_hash == generate_password_hash(password)

def validPassword(string):
    if len(string) < 8:
        return False
    return True

def validEmail(string):
    boolAddress = False
    boolDomain = False
    for i in string:
        if i == '@':
            boolAddress = True
    if (string[len(string)-4:len(string)] == '.com') or (string[len(string)-4:len(string)]) == '.org' or (string[len(string)-4:len(string)] == '.edu'):
        boolDomain = True
    return boolAddress and boolDomain
