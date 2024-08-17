#!/usr/bin/python3
"""Create a Utils file"""

# Imports
from models import User
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)

def authenticate_user(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return user
    return None

def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)