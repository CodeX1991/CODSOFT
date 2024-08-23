#!/usr/bin/python
"""The models class"""

# Imports
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    """Create contact model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        """Return the name of the contact"""
        return self.name