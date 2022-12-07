from app import myapp_obj, db
from flask import render_template, redirect, flash, url_for, request
from app.models import User, Post, Follows
from app.forms import LoginForm, HomePageForm, LogoutForm, PostsForm, SignupForm, PostForm, SearchForm, SearchResult, FollowForm, unfollowForm, unfollowForm2
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route('/')
def base():
    return render_template("base.html")

@myapp_obj.route('/profile')
@login_required
def test():
    name=data.currentLogin
    return render_template("profile.html", username=name)

@myapp_obj.route('/statistics')
@login_required
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
                    data.currentLogin = current_form.username.data 
                    login_user(user, remember=current_form.remember_me.data)
                    return redirect('/home')
            else:
                errorMessage = 'Invalid Username or Password'
    return render_template('login.html', form=current_form, error=errorMessage)

@myapp_obj.route('/logout')
@login_required
def logout():
    current_form = LogoutForm()
    logout_user()
    return render_template('base.html', form=current_form)

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
    if request.method == "POST":
        return redirect('user-profile')
    return render_template('searchResult.html', form=current_form, username=usr)

@myapp_obj.route('/user-profile', methods=['GET', 'POST'])
#@login_required
def user_profile():
    current_form = FollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET":
            name=user.username
            first=user.first
            last=user.last
            email=user.email
        if request.method == "POST":
            follow = Follows()
            current = data.currentLogin
            search = data.searchedUser
            follow.follower = current
            follow.followee = search
            db.session.add(follow)
            db.session.commit()
            return redirect('/user-profile1')
    return render_template('user-profile.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/user-profile1', methods=['GET', 'POST'])
#@login_required
def user_profile1():
    current_form = unfollowForm()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET":
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'You are now following ' + data.searchedUser
        if request.method == "POST":
            follow = Follows.query.filter_by(follower=data.currentLogin, followee=data.searchedUser)
            db.session.delete(follow)
            db.session.commit()
            return redirect('/user-profile2')
    return render_template('user-profile1.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

@myapp_obj.route('/user-profile2', methods=['GET', 'POST'])
#@login_required
def user_profile2():
    current_form = unfollowForm2()
    errormessage = ''
    users = User.query.filter_by(username=data.searchedUser)
    for user in users:
        if request.method == "GET":
            name=user.username
            first=user.first
            last=user.last
            email=user.email
            errormessage = 'You are no longer following ' + data.searchedUser
        if request.method == "POST":
            return redirect('/home')
    return render_template('user-profile2.html', form=current_form, username=name, first=first, last=last, email=email, error=errormessage)

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

@myapp_obj.route('/test')
def test2():
    follow = Follows.query.all()
    users = User.query.all()
    for user in users:
        print(follow.follower)
    return render_template('test.html')

# helper functions

class DataStore():
    searchedUser = None
    currentLogin = None

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
