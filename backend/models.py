from exts import db
from datetime import datetime 


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(30), unique=True)
    password_hash = db.Column(db.String(128))
    journals = db.relationship('Journals', backref='owner', cascade='all, delete') # deleting user deletes journal


class Journals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False) #TODO: CONFIRM UTC
    last_modified = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)