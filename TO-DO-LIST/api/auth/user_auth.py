#!/usr/bin/python3
"""Authentification Module"""

# Imports
from flask import render_template, url_for, redirect, flash
from api.forms import RegistrationForm, LoginForm, TodoForm
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from api.utils import hash_password, authenticate_user
from api.database import db
from models import User, Todo, CompleteTaskForm


# Route handling the creation of the account
@auth.route('/create-account', methods=['GET', 'POST'], strict_slashes=False)
def create_account():
    """Handle POST api/auth/create-account"""
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = hash_password(form.password.data)
        new_user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('create_account.html', title='Account registration', form=form)


# Route handling the login
@auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """Handle POST api/auth/login"""
    if current_user.is_authenticated:
         return redirect(url_for('views.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate_user(form.email.data)
        if user:
            login_user(user)
            return redirect(url_for('views.dashboard'))
    return render_template('login.html', title='Sign In', form=form)


# Logout of the session
@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have logged out successfully")
    return redirect(url_for('auth.login'))


# Handle complete task checkbox
@auth.route('/complete-task/<int:task_id>', methods=['POST'], strict_slashes=False)
@login_required
def complete_task(task_id):
    task = Todo.query.get_or_404(task_id)
    form = CompleteTaskForm()
    if form.validate_on_submit():
        task.completed = form.completed.data
        db.session.commit()
    return redirect(url_for('views.dashboard'))


# Handle add task route
@auth.route('/add', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def add():
    """Handle POST api/auth/add"""
    form = TodoForm()
    if form.validate_on_submit():
        new_task = Todo(
            task=form.task.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('views.dashboard'))
    return render_template('add_todo.html', title='Add Task', form=form, mode='add')

# Handle update task route
@auth.route('/update-task/<int:task_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update(task_id):
    task = Todo.query.get_or_404(task_id)
    # Prepopulate form with current task data
    form = TodoForm(obj=task)
    if form.validate_on_submit():
        task.task = form.task.data
        db.session.commit()
        return redirect(url_for('views.dashboard'))
    return render_template('add_todo.html', title='Update Task', form=form, task=task, mode='update')


# Handle delete task route
@auth.route('/delete-task/<int:task_id>', methods=['POST'], strict_slashes=False)
@login_required
def delete_task(task_id):
    """Handle POST api/auth/delete-task"""
    task = Todo.query.get_or_404(task_id)
    # Ensure the task belongs to the current user
    if task.user_id != current_user.id:
        return redirect(url_for('views.dashboard'))
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('views.dashboard'))

