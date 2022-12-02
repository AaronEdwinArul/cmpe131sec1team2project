from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignupForm, PostForm
from app.models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import current_user
from flask_login import login_required

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/')
    if current_form.username.data == "" or current_form.password.data == "":
        flash('ERROR: Empty input')
    a = 1
    name = 'Carlos'
    return render_template('login.html', name=name, a=a, form=current_form)



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
            return redirect('/login')        #redirect to home page when implemented

    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])
@login_required
def post():
    current_form = PostForm()
    if current_form.validate_on_submit():
        post = Post()
        text = current_form.text.data
        link = current_form.link.data
        user_id = current_user.id
        with myapp_obj.app_context():
            db.session.add(post)
            db.session.commit()
        return redirect('/home')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/')
def home():
    return render_template('base.html')



# helper functions

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

