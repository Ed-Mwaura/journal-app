from exts import db
from datetime import datetime 
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    journals = db.relationship('Journals', backref='owner', cascade='all, delete') # deleting user deletes journal

    # session operations
    def is_active(self):
        return True # for now, always active
    
    def get_id(self):
        return str(self.id)

    # CRUD Operations --create and delete for now
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Journals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False) #TODO: CONFIRM UTC
    last_modified = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)