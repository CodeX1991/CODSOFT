#!/usr/bin/python
"""The form sections that handle forms fro the models"""


# imports
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact

class RegistrationForm(UserCreationForm):
    """Generate the registration form """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

class CustomizeLoginForm(AuthenticationForm):
    """Generate the login form"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ContactForm(forms.ModelForm):
    """Generate the contact form"""
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address',]

class UpdateContactForm(forms.ModelForm):
    """Generate the update contact"""
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address',]