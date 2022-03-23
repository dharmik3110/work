from django.shortcuts import render
from sre_constants import SUCCESS
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login,LoginView
from .forms import OwnerForm

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')

def contacts(request):
    return render(request,'contacts.html')

def forpgowner(request):
    return render(request,'forpgowner.html')

def aboutus(request):
    return render(request,'aboutus.html')




  
