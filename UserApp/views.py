from cgitb import html
from pyexpat import model
from sre_constants import SUCCESS
from django.conf import settings
# from django.shortcuts import render, render_to_response
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login,LoginView,LogoutView

from UserApp.models import FinderRegistration1, OwnerRegistration1, User
from .forms import FinderRegistrationForm, OwnerRegistrationForm, UserForm
from django.contrib.auth import login,logout
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


# Create your views here.

class OwnerRegisterView(CreateView):

    model = User
    form_class = OwnerRegistrationForm
    template_name = 'ownerportal/registration.html'

  
    def get_context_data(self, **kwargs):
        kwargs['user_type']='owner'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request,user) 
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        dict = {'username': username , 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content = render_to_string('email.html',dict)
        text_contant = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject,text_contant,from_email,[to])
        msg.attach_alternative(html_content,"text/html")
        msg.send()      
        return redirect('/userapp/login')

   

    #def get_success_message(self, cleaned_data):
        #username = cleaned_data["owner"]
        #return username + " - owner Created Successfully..!!"

class FinderRegisterView(CreateView):

    model = User
    form_class = FinderRegistrationForm
    template_name = 'userportal/registration.html'
    

    def get_context_data(self, **kwargs):
        kwargs['user_type']= 'finder'
        return super().get_context_data(**kwargs)
  
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        dict = {'username': username , 'password1': password1}
        subject, from_email, to = 'subject', settings.EMAIL_HOST_USER, form.cleaned_data.get('email')
        html_content = render_to_string('email.html',dict)
        text_contant = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject,text_contant,from_email,[to])
        msg.attach_alternative(html_content,"text/html")
        msg.send()
        return redirect('/userapp/login')
       

    #def get_success_message(self, cleaned_data):
        #username = cleaned_data["finder"]
        #return username + " - finder Created Successfully..!!"


class UserLogin1(LoginView):
    template_name = "userportal/login.html"
    
    def get(self, request, *args, **kwargs): 
        print(self.request.user)
        return self.render_to_response(self.get_context_data())


class LogoutView(LogoutView):
    def get(self, request):
        logout(self.request.user)
        return redirect('/homepage')
    
  