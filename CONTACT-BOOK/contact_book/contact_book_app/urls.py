#!/usr/bin/python
"""Url Module that generate urls for the views"""


# imports
from django.urls import path
from contact_book_app import views

urlpatterns = [
    path("", views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("login/", views.CustomizeLoginView.as_view(), name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("register/", views.register, name='register'),
    path("add_contact/", views.add_contact, name='add_contact'),
    path("update/<int:contact_id>/", views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]