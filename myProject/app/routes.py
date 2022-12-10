from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignupForm, PostForm, ProfileEditForm
from app.models import User, Post, Likes, Follows #load_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from flask_login import current_user, login_user, logout_user, login_required


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
        post.text = current_form.text.data
        post.link = current_form.link.data
        post.user_id = current_user.id
        with myapp_obj.app_context():
            db.session.add(post)
            db.session.commit()
        return redirect('/home')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/profile', methods = ['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html')


@myapp_obj.route('/profile_edit', methods = ['POST','GET'])
@login_required
def profile_edit(_):
    current_form = ProfileEditForm()
    errorMessage = ''
    if current_form.validate_on_submit():
        if not(validDOB(current_form.dob.data)):
            errorMessage = 'DOB must be in yyyy-mm-dd format.'
        else:
            user = User.query.filter_by(current_user.id).first()
            user.dob = current_form.dob.data
            user.location = current_form.location.data
            user.bio = current_form.bio.data
            db.session.add(user)
            db.session.commit()
            return redirect('/profile') #redirects to profile after submitting form, will show updated bio, dob, location
    return render_template('profile.html', form=current_form, error = errorMessage)


@myapp_obj.route('/delete_account', methods = ['DELETE'])
@login_required
def delete_account():

    user = User.query.filter_by(current_user.id).first()
    
    user_posts = Post.query.filter_by(current_user.id).all()
    user_likes = Likes.query.filter_by(current_user.id).all()
    user_follows = Follows.query.filter_by(current_user.id).all()
    
    db.session.delete(user)   
    
    for u in user_posts:
        db.session.delete(u)
    for u in user_likes:
        db.session.delete(u)
    for u in user_follows:
        db.session.delete(u)
    
    db.session.commit()
    logout_user()
    user = None 
    user_posts = None
    user_likes = None
    user_follows = None 

    return render_template('signup.html')


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

def validDOB(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("DOB should be in YYYY-MM-DD")


