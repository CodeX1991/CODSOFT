from django import forms
from .models import User

# Create yor form here
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']