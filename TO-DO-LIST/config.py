#!/usr/bin/python3
"""Flask todo-app config module"""

DB_NAME = 'todo_db'

class Config:
    SECRET_KEY = 'codsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'  # Flask-Caching related config

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}_dev.db'.format(DB_NAME)
