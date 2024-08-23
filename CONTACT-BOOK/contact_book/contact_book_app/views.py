#!/usr/bin/python
"""View Module that handle all views"""

# Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Contact
from django.db.models import Q
from .forms import RegistrationForm, CustomizeLoginForm, ContactForm, UpdateContactForm


# Create your views here.
def home(request):
    """Handle home route"""
    return render(request, 'contact_book_app/home.html', {})

def register(request):
    """Handle register route"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'contact_book_app/register.html', {'form': form})

class CustomizeLoginView(LoginView):
    """Handle login route using LoginView"""
    template_name = 'contact_book_app/login.html'
    authentication_form = CustomizeLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('dashboard')

def logout_view(request):
    logout(request)
    return redirect('home') 

@login_required
def dashboard(request):
    """Handle dashboard route"""
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(
            Q(name__icontains=query) | Q(phone_number__icontains=query),
            user=request.user
        )
    else:
        contacts = request.user.contacts.all()
    user = request.user
    return render(request, 'contact_book_app/dashboard.html', {'contacts': contacts, 'user': user, 'query': query})

@login_required
def add_contact(request):
    """Handle add contact route"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('dashboard')
    else:
        form = ContactForm()
    return render(request, 'contact_book_app/add_contact.html', {'form': form})

@login_required
def update_contact(request, contact_id):
    """Handle update/<int:contact_id>"""
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateContactForm(instance=contact)
    return render(request, 'contact_book_app/update_contact.html', {'form': form})

@login_required
def delete_contact(request, contact_id):
    """Handle delete/<int:contact_id>"""
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)
    if request.method == 'POST':
            contact.delete()
            return redirect('dashboard')
    return render(request, 'contact_book_app/delete_contact.html', {'contact': contact})