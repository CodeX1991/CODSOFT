#!/usr/bin/python3
"""Endpoints for the views"""

# Imports
from api.views import views
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from models import Todo, CompleteTaskForm


@views.route('/')
def home():
    return redirect(url_for('auth.login'))

@views.route('/dashboard')
@login_required
def dashboard():

    # Create an instance of the form
    form = CompleteTaskForm()
    # Retrieve the session id
    user_id = current_user.id

    # Query the database for todos belonging to the current user
    todos = Todo.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', title='dashboard', user=current_user, todos=todos, form=form)