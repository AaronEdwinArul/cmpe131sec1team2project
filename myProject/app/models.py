from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first = db.Column(db.String)
    last = db.Column(db.String)
    email = db.Column(db.String(32), unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String(200))

    posts = db.relationship('Post', backref='author', lazy='dynamic')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.String(1000))
    link = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
