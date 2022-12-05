from app import myapp_obj, db
from flask import render_template, redirect, flash, url_for, request
from app.models import User, Post, Follows#, Likes
from app.forms import LoginForm, HomePageForm, LogoutForm, PostsForm, SignupForm, PostForm, SearchForm, SearchResult, FollowForm
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route('/')
def base():
    return render_template("base.html")

@myapp_obj.route('/profile')
def test():
    users = User.query.all()
    for user in users:
        name=user.username
    return render_template("profile.html", username=name)

@myapp_obj.route('/statistics')
def test1():
    return render_template("statistics.html")
    
@myapp_obj.route('/private')
@login_required
def private():
    return 'Hi this is a private page'

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
                    login_user(user, remember=current_form.remember_me.data)
                    return redirect('/home')
            else:
                errorMessage = 'Invalid Username or Password'
    return render_template('login.html', form=current_form, error=errorMessage)

@myapp_obj.route('/logout')
def logout():
    logout_user()
    return render_template('base.html')

@myapp_obj.route('/home', methods=['POST', 'GET'])
@login_required
def home():
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
            user.first = current_form.first.data
            user.last = current_form.last.data
            user.email = current_form.email.data
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')        #redirect to login page when implemented

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

@myapp_obj.route('/search', methods = ['POST','GET'])
#@login_required
def search():
    current_form = SearchForm()
    errormessage = ''
    if request.method == "GET":
        return render_template('search.html', form = current_form)
    if request.method == "POST":
        searched = request.form["username"]
        users = User.query.all()
        for user in users:
            if user.username == searched:
                data.searchedUser=searched                
                return redirect(url_for("user", usr=searched))
            else: 
                errormessage = 'User not found'
    else: 
        errormessage = 'User not found'  
    return render_template('search.html', error = errormessage)

@myapp_obj.route('/user/<usr>', methods = ['POST','GET'])
def user(usr):
    current_form = SearchResult()
    return render_template('searchResult.html', form=current_form, username=usr)

@myapp_obj.route('/user-profile', methods=['GET', 'POST'])
#@login_required
def user_profile():
    current_form = FollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        name=user.username
        first=user.first
        last=user.last
        email=user.email
        '''if current_form.validate_on_submit():
            follow = Follows()
            follow.follower_id = 1
            follow.following_id = user.id
            db.session.add(follow)
            db.session.commit()
            print('followed')
        if current_form.validate_on_submit():
            follow.follower_id = 0
            follow.following_id = ''
            db.session.remove(follow)
            db.session.commit()
            print('unfollowed')'''
    return render_template('user-profile.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

# helper functions

class DataStore():
    searchedUser = None

data = DataStore()

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