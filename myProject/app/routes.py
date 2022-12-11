
from app import myapp_obj, db
from flask import render_template, redirect, flash, url_for, request
from app.models import Likes, User, Post, Follows
from app.forms import LoginForm, HomePageForm, LogoutForm, PostsForm, SignupForm, PostForm, SearchForm, SearchResult, FollowForm, unfollowForm, unfollowForm2, ProfileEditForm, Delete_Account_Form

#importing spanish forms
from app.forms import Delete_Account_Form_Spanish, ProfileEditForm_Spanish, ProfileForm_Spanish

from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
import datetime

@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    errorMessage = ''
    if current_form.validate_on_submit():
        users = User.query.all()
        for user in users:
            if user.username == current_form.username.data:
                if check_password_hash(user.password,current_form.password.data):
                    if current_form.remember_me.data:
                        login_user(user, remember=True)
                    data.currentLogin = current_form.username.data 
                    login_user(user, remember=current_form.remember_me.data)
                    return redirect('/home')
            else:
                errorMessage = 'Invalid Username or Password'
    return render_template('login.html', form=current_form, error=errorMessage)


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
    return render_template('profile_edit.html', form=current_form, error = errorMessage)
"""
@myapp_obj.route('/followers', methods=['GET', 'POST'])
def followers():
    errormessage = ''
    follow = Follows.query.filter_by(followee=data.currentLogin)
    if request.method == "GET":
        for user in follow:
            errormessage = "You are being followed by " + follow.followee
        else:
            errormessage = 'No one is following you :('
    return render_template('followers.html', error=errormessage)

@myapp_obj.route('/following', methods=['GET', 'POST'])
def following():
    errormessage = ''
    follower = Follower.query.filter_by(follower=data.currentLogin)
    if request.method == "GET":
        for user in following:
            errormessage = "You are following" + follow.following
        else:
            errormessage = 'You are not following anyone.'
    return render_template('following.html', error=errormessage)





"""


@myapp_obj.route('/delete_account', methods = ['GET', 'POST'])
@login_required
def delete_account():
    current_form = Delete_Account_Form()
    if current_form.validate_on_submit():

        if current_user.password == current_form.password.data: #checks if entered password is equal to current_users' password, if true deletes account, if false returns error
            user = User.query.filter_by(current_user.id).first()
                
            user_posts = Post.query.filter_by(current_user.id).all()
            user_likes = Likes.query.filter_by(current_user.id).all()
            user_follows = Follows.query.filter_by(current_user.id).all()
                
                
            for u in user_posts:
                    db.session.delete(u)
            for u in user_likes:
                    db.session.delete(u)
            for u in user_follows:
                    db.session.delete(u)
                    
            db.session.delete(user)   
            db.session.commit()
            print("Your account has been deleted. Redirecting to the login page...")
            return redirect('/login')

        else:
            print("Incorrect Password!")

    return render_template('delete_account.html')


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
        raise ValueError("DOB should be in YYYY-MM-DD") #checks if DOB is in yyyy-mm-dd format

#Spanish 

@myapp_obj.route('/profile_spanish', methods = ['POST', 'GET'])
@login_required
def profile_spanish():
    return render_template('profile_spanish.html')


@myapp_obj.route('/profile_edit_spanish', methods = ['POST','GET'])
@login_required
def profile_edit_spanish(_):
    current_form = ProfileEditForm_Spanish()
    errorMessage = ''
    if current_form.validate_on_submit():
        if not(validDOB(current_form.dob.data)):
            errorMessage = 'La fecha de nacimiento debe estar en formato aaaa-mm-dd.'
        else:
            user = User.query.filter_by(current_user.id).first()
            user.dob = current_form.dob.data
            user.location = current_form.location.data
            user.bio = current_form.bio.data
            db.session.add(user)
            db.session.commit()
            return redirect('/profile_spanish') #redirects to profile after submitting form, will show updated bio, dob, location
    return render_template('profile_edit_spanish.html', form=current_form, error = errorMessage)

@myapp_obj.route('/delete_account_spanish', methods = ['GET', 'POST'])
@login_required
def delete_account_spanish():
    current_form = Delete_Account_Form_Spanish()
    if current_form.validate_on_submit():

        if current_user.password == current_form.password.data: #checks if entered password is equal to current_users' password, if true deletes account, if false returns error
            user = User.query.filter_by(current_user.id).first()
                
            user_posts = Post.query.filter_by(current_user.id).all()
            user_likes = Likes.query.filter_by(current_user.id).all()
            user_follows = Follows.query.filter_by(current_user.id).all()
                
                
            for u in user_posts:
                    db.session.delete(u)
            for u in user_likes:
                    db.session.delete(u)
            for u in user_follows:
                    db.session.delete(u)
                    
            db.session.delete(user)   
            db.session.commit()
            print("Tu cuenta ha sido eliminada. Redirigiendo a la página de inicio de sesión...")
            return redirect('/login_spanish')

        else:
            print("Contraseña incorrecta!")

    return render_template('delete_account_spanish.html')

