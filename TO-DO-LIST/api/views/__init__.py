#!/usr/bin/python3
"""Create a Blueprint for todo routes"""

from flask import Blueprint

views = Blueprint('views', __name__)

# Import routes to register with the Blueprint
from api.views import todo_views