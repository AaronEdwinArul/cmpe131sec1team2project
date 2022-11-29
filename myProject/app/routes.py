from app import myapp_obj
from flask import render_template, redirect, flash
from app.forms import LoginForm
from app.forms import SignupForm


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

    if current_form.validate_on_submit():
        return redirect('/')        #redirect to home page when implemented
    
    if current_form.first.data == "":
        flash('ERROR: Empty input')
    elif current_form.last.data == "":
        flash('ERROR: Empty input')
    elif current_form.email.data == "":
        flash('ERROR: Empty input')
    elif current_form.username.data == "":
        flash('ERROR: Empty input')
    elif current_form.password.data == "":
        flash('ERROR: Empty input')
        
    '''if validEmail(current_form.email.data):
        flash('ERROR: Invalid email address')'''
    '''
    name email password will be stored with hash
    rest will be stored normally in databsae
    '''
    return render_template('signup.html',form=current_form)


@myapp_obj.route('/')
def home():
    return render_template('base.html')

def validEmail(string):
    str = string
    valid = False
    for i in str:
        if i == '@':
            valid = True
    return valid