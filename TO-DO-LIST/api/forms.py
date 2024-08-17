#!/usr/bin/python3
"""Flask todo-app form class"""

# Imports
from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User
from .utils import verify_password

# form for registration
class RegistrationForm(FlaskForm):
    """Create RegistrationForm class form"""
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Enter your firstname"})
    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=4, max=20)],render_kw={"placeholder": "Enter your lastname"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            flash('Email is already taken. Please choose a different one.', 'error')
            raise ValidationError('Email is already taken. Please choose a different one.')

# Login Form       
class LoginForm(FlaskForm):
    """Create LoginForm class form"""
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Enter your password"})
    submit = SubmitField('Sign in')

    def validate_email(self, email):
        """Verify the email field from the form"""
        user = User.query.filter_by(email=email.data).first()
        if not user:
            flash('Email is does not exist, check the email and try again.', 'error')
            raise ValidationError('Email is does not exist, check the email and try again')

    def validate_password(self, password):
        """Verify the password field from the form"""
        user = User.query.filter_by(email=self.email.data).first()
        if user and not verify_password(user.password, password.data):
            flash('Incorrect password, try again.', 'error')
            raise ValidationError('Incorrect password, try again.')
        
# TodoForm
class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired(), Length(min=1, max=200)])
    completed = BooleanField('Completed')
    submit = SubmitField('Add Task')
