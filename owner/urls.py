import imp
from unicodedata import name
from django.urls import path
from owner import views
from os import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

#app_name = 'owner_urls'

    
   
urlpatterns = [
   
   
    path('homepage',views.homepage, name='homepage'),
    path('contacts',views.contacts, name='contacts'),
    path('forpgowner',views.forpgowner, name='forpgowner'),
    path('aboutus',views.aboutus, name='aboutus'),
   
]
    

    



   


	
