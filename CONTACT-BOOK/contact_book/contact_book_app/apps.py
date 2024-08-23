#!/usr/bin/python
"""Entry point to the django app"""

# Imports
from django.apps import AppConfig


class ContactBookAppConfig(AppConfig):
    """Create config class"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_book_app'
