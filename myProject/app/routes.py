from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.models import User, Post
from app.forms import LoginForm
from app.forms import HomePageForm
from app.forms import LogoutForm
from app.forms import PostsForm
from app.forms import SignupForm
from app.forms import PostForm
import itertools
from datetime import date
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

@myapp_obj.route('/')
def test2():
    return render_template("base.html")

@myapp_obj.route('/profile')
def test():
    return render_template("profile.html")

@myapp_obj.route('/statistics')
def test1():
    return render_template("statistics.html")
    
@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

@myapp_obj.route('/logout')
@login_required
def logout():
    load_user(current_user)
    return redirect('/login')


@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    # taking input from the user and doing somithing with it
    if current_form.validate_on_submit():
        # search to make sure we have the user in our database
        user = User.query.filter_by(username=current_form.username.data).first()

        # check user's password with what is saved on the database
        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            # if passwords don't match, send user to login again
            return redirect('/login')

        # login user
        login_user(user, remember=current_form.remember_me.data)
        flash('quick way to debug')
        flash('another quick way to debug')
        print(current_form.username.data, current_form.password.data)
        return redirect('/home')
    a = 1
    name = 'Username'
    return render_template('login.html', name=name, a=a, form=current_form)


@myapp_obj.route('/home', methods=['POST', 'GET'])
def home():
    a = 8
    name = 'Friend'
    current_form = HomePageForm()
    if current_form.validate_on_submit():
       return redirect('/home')
    return render_template('home.html', form=current_form)

@myapp_obj.route('/members/<string:name>/')
def getMemberName(name):
    return escape(name)

@myapp_obj.route('/default')
def getDefault(name):
    return redirect('/home')

@myapp_obj.route('/posts')
def getPosts():
    current_form = PostsForm()
    return render_template('posts.html', form=current_form)

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
            user.email = current_form.email.data
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')        #redirect to home page when implemented

    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])
#@login_required
def post():
    '''
    to do:
    change user_id line when login status is implemented
    '''
    current_form = PostForm()
    if current_form.validate_on_submit():
        post = Post()
        post.post = current_form.text.data  #save body text to db
        post.link = current_form.link.data  #save image url to db
        post.user_id = 1    #change to current user later on
        today = date.today()
        post.date = str(today).replace('-','')      #date of post stored as yyyymmdd
        with myapp_obj.app_context():       #add object to db
            db.session.add(post)
            db.session.commit()
        return redirect('/feed')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/feed', methods = ['POST','GET'])
def view():

    '''
    to do:
    print username of author when login is implemented and current user can be found
    connect viewable posts to following list when implemented
    '''

    #create form for redirecting to another page
    post = Post.query.all()     #query all posts
    posts = []                  #list of dictionaries
    for i in post:              #iterate through all queries
        text = {}               #create a dictionary of 'body':'text'
        text['body'] = i.post
        text['link'] = i.link
        posts.append(text)      #add individual dictionaries to array
    #/feed page will display each body text and have access to the link to show the image
    return render_template('feed.html', posts = posts)



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



