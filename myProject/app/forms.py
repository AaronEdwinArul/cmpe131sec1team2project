from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from datetime import date

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

class LikeForm(FlaskForm):
    submit = SubmitField('Like')

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


#SPANISH VERSION
class SLoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    remember_me = BooleanField('Acuérdate de mí')
    submit = SubmitField('Registrarse')

class SSignupForm(FlaskForm):
    first = StringField('Primer nombre', validators=[DataRequired()])
    last = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    submit = SubmitField('Crear una cuenta')

class SHomePageForm(FlaskForm):
    submitHome = SubmitField('Hogar')
    
class SLogoutForm(FlaskForm):
    submitLogout = SubmitField('Cerrar sesión')

class SPostsForm(FlaskForm):
    refreshPosts = SubmitField('Publicaciones')

class SPostForm(FlaskForm):
    text = TextAreaField('Entra mensaje')
    link = TextAreaField('URL de la imagen (opcional)')
    post = SubmitField('¡Publicación!')

class SSearchForm(FlaskForm):
    username = StringField('Nombre de usuario')
    submit = SubmitField('Búsqueda')

class SSearchResult(FlaskForm):
    username = StringField('Nombre de usuario')

class SFollowForm(FlaskForm):
    username = StringField('Nombre de usuario')
    submit = SubmitField('Seguir')

class SunfollowForm(FlaskForm):
    submit = SubmitField('Dejar de seguir')

class SunfollowForm2(FlaskForm):
    submit = SubmitField('Hogar')


