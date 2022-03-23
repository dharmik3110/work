from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'email', 'phone_number', 'is_superuser', 'is_staff', 'is_owner', 'is_finder')
    list_display = ("username", "email", "is_staff")
    list_filter =  ("is_staff" , "created_at","updated_at",)

