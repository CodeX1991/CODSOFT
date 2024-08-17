#!/usr/bin/python3
"""Run the flask todo-app"""
from api import create_todo_app

app = create_todo_app('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run(debug=True)