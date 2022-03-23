from django import forms
from django.contrib.auth.models import User
from .models import *

class OwnerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = OwnerRegistration
        fields = ('ownername', 'password','email','phone_number')


class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = OwnerRegistration
        fields = ("ownername", "password", "email", "phone_number",)

CHOICES = (
        ("H", "Home"),
        ("W", "Work"),
    )
    
