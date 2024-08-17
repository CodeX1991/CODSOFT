#!/usr/bin/python3
"""Create a Blueprint for todo routes"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

# Import routes to register with the Blueprint
from api.auth import user_auth