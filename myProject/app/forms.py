from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class SignupForm(FlaskForm):
    first = StringField('First Name', validators=[DataRequired()])
    last = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    submit = SubmitField('Create Account')

class PostForm(FlaskForm):
    text = TextAreaField('Enter message here')
    link = TextAreaField('Image URL (Optional)')
    post = SubmitField('Post!')

class ProfileEditForm(FlaskForm):
    dob = StringField('yyyy-mm-dd')
    location = StringField('Location')
    bio = StringField('Bio')

class LogoutForm(FlaskForm):
    submitLogout = SubmitField('Logout')

class ProfileForm(FlaskForm):
    submitProfileForm = SubmitField('Profile')



