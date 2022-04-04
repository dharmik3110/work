from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import  RegexValidator
from generic.models import Basefield

class User(Basefield,AbstractUser):

# Create your models here.

   is_owner= models.BooleanField(default=False)
   is_finder= models.BooleanField(default=False)
 

   class Meta():
       db_table="User"
       

class OwnerRegistration1(User,Basefield):

# Create your models here.

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='owner')
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True) 

    class Meta():
        db_table = "Owner1"

   
class FinderRegistration1(User,Basefield):

# Create your models here.

    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='finder')
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True) 

    class Meta():
        db_table = "finder"

    




