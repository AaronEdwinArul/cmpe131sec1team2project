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
    liked = db.relationship('Likes', backref = 'liking',lazy = 'dynamic')
    #follows = db.relationship('Follows', backref = 'following', lazy = 'dynamic')

    bio = db.Column(db.String)
    dob = db.Column(db.String)
    location = db.Column(db.String) 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post = db.Column(db.String(500))
    link = db.Column(db.String(200))
    date = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    liked = db.relationship('Likes', backref = 'original', lazy = 'dynamic')

    comments = db.relationship('Comments', backref = 'parent', lazy = 'dynamic')
    
    def get_author(self, num):
        author = User.query.filter_by(id = num).first()
        if not author == None:
            return author.username
        else:
            return 'Unknown User'

class Likes(db.Model):
    # 2 wide table that lists users who liked (left) a post (right)
    # posts are labelled by id
    liker = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    post = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key = True)

class Follows(db.Model):
    # 2 wide table that lists followers (left) of followee (right)
    # e.g. if x and y both follow each other, and z follows x
    # Table:    x | y
    #           y | x
    #           z | x
    follower = db.Column(db.String,primary_key = True)#, db.ForeignKey('user.id'), primary_key = True)
    followee = db.Column(db.String)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
