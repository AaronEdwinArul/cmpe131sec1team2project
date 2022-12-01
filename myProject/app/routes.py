from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm, SignupForm, PostForm
'''from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

#private login
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_login import load_user'''

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
            return redirect('/login')        #redirect to home page when implemented

    '''
    name email password will be stored with hash
    rest will be stored normally in databsae
    '''
    return render_template('signup.html',form=current_form, error = errorMessage)

@myapp_obj.route('/post', methods = ['POST','GET'])
def post():
    current_form = PostForm()

    '''
    field for text entry
    button to attach image
    button pressed -> show field for link text
    html displays image from link
    '''
    return render_template('post.html')

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

