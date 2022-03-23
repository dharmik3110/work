from django.contrib import admin

from owner.models import OwnerRegistration

# Register your models here.

@admin.register(OwnerRegistration)
class OwnerAdmin(admin.ModelAdmin):
    fields = ("username","password", "email",  "phone_number", )
    list_display = ("ownername", "email")
    list_filter =  ("created_at","updated_at",)




