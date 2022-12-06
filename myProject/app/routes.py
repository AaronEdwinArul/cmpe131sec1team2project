from app import myapp_obj, db
from flask import render_template, redirect, flash
from app.models import User, Post, load_user#, Likes, Follows
from app.forms import LoginForm, HomePageForm, LogoutForm, PostsForm, SignupForm, PostForm
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user,login_required,login_user,logout_user

@myapp_obj.route('/')
def base():
    db.create_all()
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
def logout():
    #load_user(current_user)
    logout_user()
    return redirect('/login')


@myapp_obj.route('/login', methods=['POST', 'GET'])
def login():
    current_form = LoginForm()
    errorMessage = ''
    
    if current_form.validate_on_submit():   #on submission,
        user = User.query.filter_by(username=current_form.username.data).first()    
        if not user == None:        #check if user exists in database
            if check_password_hash(user.password,current_form.password.data):   #check is password is correct
                login_user(user, current_form.remember_me.data) #if true, login
                return redirect('/home')
        else:
            errorMessage = 'Invalid Username of Password'       #else, raise error message 
    return render_template('login.html', form=current_form, errorMessage=errorMessage)


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
    if current_form.validate_on_submit():           #on form submission,
        if not(validPassword(current_form.password.data)):  #check if password is long enough
            errorMessage = 'Password must be longer than 8 characters'
        elif not(validEmail(current_form.email.data)):      #simple email check
            errorMessage = 'Invalid email address (must have domain .com,.org,.edu)'
        else:
            user = User()       #create db object with user's first & last name, email, username, password
            user.first = generate_password_hash(current_form.first.data)
            user.last = generate_password_hash(current_form.last.data)
            user.email = current_form.email.data
            user.username = current_form.username.data
            user.password = generate_password_hash(current_form.password.data)
            db.session.add(user)        #add user to database
            db.session.commit()
            return redirect('/login')        #redirect to home page when implemented

    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])
@login_required
def post():
    current_form = PostForm()
    if current_form.validate_on_submit():
        post = Post()
        post.post = current_form.text.data  #save body text to db
        post.link = current_form.link.data  #save image url to db
        post.user_id = current_user.id      #save current user's id to track poster
        today = date.today()
        post.date = str(today).replace('-','')      #date of post stored as yyyymmdd
        with myapp_obj.app_context():       #add object to db
            db.session.add(post)
            db.session.commit()
        return redirect('/feed')        #redirects to home after posting, will show post
    return render_template('post.html', form = current_form)

@myapp_obj.route('/feed', methods = ['POST','GET'])
#@login_required
def view():

    '''
    to do:
    implement likes
    connect viewable posts to following list when implemented
    '''

    #create form for redirecting to another page
    post = Post.query.all()     #query all posts
    posts = []                  #list of dictionaries
    for i in post:              #iterate through all queries
        text = {}               #create a dictionary of 'body':'text', etc.
        text['body'] = i.post
        text['link'] = i.link
        text['id'] = i.user_id
        text['author'] = i.get_author(i.user_id)
        text['date'] = i.date
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