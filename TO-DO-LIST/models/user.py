
#!/usr/bin/python3
"""Database model for user account"""

# Import modules
from api.database import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField

# User model class
class User(db.Model, UserMixin):
    """User's Table"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    
    # One-to-Many relationship: One user can have many to-do lists
    todos = db.relationship('Todo', backref='user', lazy=True)
    
# Task Model class
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Task Complete task form
class CompleteTaskForm(FlaskForm):
    completed = BooleanField('completed')
    submit = SubmitField('Update')