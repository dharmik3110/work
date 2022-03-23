from os import name
from django.urls import path
from .views import *


app_name = 'UserApp_urls'

urlpatterns = [
    
    path("user-registration/",FinderRegisterView.as_view(),name="user-registration"),
    path("owner-registration/",OwnerRegisterView.as_view(),name="owner-registration"),
    path('login/',UserLogin1.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),

]