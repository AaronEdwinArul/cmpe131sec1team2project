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
    link = TextAreaField('Image URL')
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

class ProfileEditForm(FlaskForm):
    dob = StringField('yyyy-mm-dd')
    location = StringField('Location')
    bio = StringField('Bio')
    submit = SubmitField('Save')

class ProfileForm(FlaskForm):
    submit= SubmitField('Profile')

class Delete_Account_Form(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Delete Account')


#SPANISH VERSION

class SLoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    remember_me = BooleanField('Acu??rdate de m??')
    submit = SubmitField('Registrarse')

class SSignupForm(FlaskForm):
    first = StringField('Primer nombre', validators=[DataRequired()])
    last = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Correo electr??nico', validators=[DataRequired()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Clave', validators=[DataRequired()])
    submit = SubmitField('Crear una cuenta')
    
class SLogoutForm(FlaskForm):
    submitLogout = SubmitField('Cerrar sesi??n')

class SPostsForm(FlaskForm):
    refreshPosts = SubmitField('Publicaciones')

class SPostForm(FlaskForm):
    text = TextAreaField('Entra mensaje')
    link = TextAreaField('URL de la imagen (opcional)')
    post = SubmitField('??Publicaci??n!')

class SSearchForm(FlaskForm):
    username = StringField('Nombre de usuario')
    submit = SubmitField('B??squeda')

class SSearchResult(FlaskForm):
    username = StringField('Nombre de usuario')

class SFollowForm(FlaskForm):
    username = StringField('Nombre de usuario')
    submit = SubmitField('Seguir')

class SunfollowForm(FlaskForm):
    submit = SubmitField('Dejar de seguir')

class SunfollowForm2(FlaskForm):
    submit = SubmitField('Hogar')

class ProfileEditForm_Spanish(FlaskForm):
    dob = StringField('yyyy-mm-dd')
    location = StringField('Ubicaci??n:')
    bio = StringField('Biograf??a')
    submit = SubmitField('Ahorrar')

class Delete_Account_Form_Spanish(FlaskForm):
    password = PasswordField('Clave', validators=[DataRequired()])
    submit= SubmitField('Eliminar Cuenta')

class ProfileForm_Spanish(FlaskForm):
    submit= SubmitField('Perfil')