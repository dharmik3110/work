from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login,LoginView

from UserApp.models import FinderRegistration1, User
from .forms import FinderRegistrationForm, OwnerRegistrationForm, UserForm
from django.contrib.auth import login,logout


# Create your views here.

class OwnerRegisterView(CreateView):

    form_class = OwnerRegistrationForm
    template_name = 'ownerportal/registration.html'
    model = User
  
    def form_valid(self, form):
        user = form.save()
        login(self.request,User)     
        user.save()    
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['user_type']='owner'
        return super().get_context_data(**kwargs)

    #def get_success_message(self, cleaned_data):
        username = cleaned_data["owner"]
        return username + " - owner Created Successfully..!!"

class FinderRegisterView(CreateView):

    form_class = FinderRegistrationForm
    template_name = 'userportal/registration.html'
    model = User

    def get_context_data(self, **kwargs):
        kwargs['user_type']='finder'
        return super().get_context_data(**kwargs)
  
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        return redirect('/userapp/login')
        #return LoginView.as_view()(template_name='Userportal/login.html')
    

    #def get_success_message(self, cleaned_data):
        #username = cleaned_data["finder"]
        #return username + " - finder Created Successfully..!!"


class UserLogin1(LoginView):
    template_name = "userportal/login.html"
    
    def get(self, request, *args, **kwargs): 
        print(self.request.user)
        return self.render_to_response(self.get_context_data())


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/homepage')
    
  