from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "password","email","phone_number")
        
class AdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ("username", "password", "email", "is_superuser", "is_staff", "is_active","phone_number")


class OwnerRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.save()
        return user




class FinderRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password', 'email', 'is_superuser', 'is_staff', 'is_active')


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_finder = True
        user.save()
        return user