from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class HomePageForm(FlaskForm):
    submitHome = SubmitField('Home')
    
class LogoutForm(FlaskForm):
    submitLogout = SubmitField('Logout')

class PostsForm(FlaskForm):
    refreshPosts = SubmitField('Posts')

