from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
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

class SearchForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Search')

class SearchResult(FlaskForm):
    username = StringField('Username')

class FollowForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Follow')

class unfollowForm(FlaskForm):
    submit = SubmitField('Unfollow')

class unfollowForm2(FlaskForm):
    submit = SubmitField('Home')

class ProfileEditForm(FlaskForm):
    dob = StringField('yyyy-mm-dd')
    location = StringField('Location')
    bio = StringField('Bio')

class ProfileForm(FlaskForm):
    submit= SubmitField('Profile')

class Delete_Account_Form():
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Delete Account')


#Spanish Forms

class ProfileEditForm_Spanish(FlaskForm):
    dob = StringField('yyyy-mm-dd')
    location = StringField('Ubicación:')
    bio = StringField('Biografía')

class Delete_Account_Form_Spanish():
    password = PasswordField('Clave', validators=[DataRequired()])
    submit= SubmitField('Eliminar Cuenta')

class ProfileForm_Spanish(FlaskForm):
    submit= SubmitField('Perfil')
