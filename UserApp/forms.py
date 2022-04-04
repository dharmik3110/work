from dataclasses import field
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
        model =  User
        fields = ("username", "password", "email",'phone_number', "is_superuser", "is_staff", "is_active")


class OwnerRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(required=True, max_length=10)
    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_owner = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        
        return user

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].help_text=None
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None




class FinderRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_finder = True
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        return user

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].help_text=None
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None

