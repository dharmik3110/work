#from pickle import TRUE

from django.db import models
from generic.models import Basefield
import imp
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import  RegexValidator
from generic.models import Basefield

# Create your models here.


'''
class Role(Basefield):
    role_name = models.CharField(max_length=30)	
    class Meta():
        db_table = "Role"

	

class User(Basefield):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=7)
    user_address = models.CharField(max_length=50)
    user_phonenumber = models.CharField(max_length=10)
    user_age = models.IntegerField(max_length=3,NULL = True)
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE)
    class Meta():
        db_table = "user"


class owner(Basefield):
    owner_name = models.CharField(max_length=30)
    owner_email = models.EmailField(max_length=254)
    owner_phonenumber = models.CharField(max_length=10)
    role_id = models.ForeignKey(Role,on_delete=models.CASCADE)

    class Meta():
        db_table = "owner"

class  Rooms(Basefield):
    room_name = models.CharField(max_length=30)
    room_availability = models.BooleanField(default=True) 
    room_type = models.CharField(max_length=30, null=True)
    room_sharing = models.CharField(max_length=30)

    class Meta():
        db_table = "roomcat"


class State(Basefield):
	state_id = models.IntegerField(primary_key=True)
	state_name = models.CharField(max_length=30)
	state_code = models.CharField(max_length=30)
	class Meta():
         db_table = "state"

class City(Basefield):
	city_id = models.IntegerField(primary_key=True)
	city_name = models.CharField(max_length=30)
	city_code = models.CharField(max_length=30)
	class Meta():
         db_table = "city"

class Address(Basefield):
    address = models.CharField( max_length=50)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    class Meta():
            db_table = "address"

class Pg(Basefield):
    pg_name = models.CharField(max_length=30)
    pg_address = models.ForeignKey(Address,on_delete=models.CASCADE)
    pg_availability = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    pg_rooms = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    class Meta():
            db_table = "pg"


'''

class OwnerRegistration(Basefield):

# Create your models here.

    ownername = models.CharField(max_length = 99, unique = True)
    password = models.CharField(max_length=50, blank=False, default=False)
    email = models.EmailField(_('email address') ,max_length=150, unique=True)
    #phone_number = PhoneNumberField(unique=True,null=False, region = 'IN')
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, unique=True) 
   
    OWNERNAME_FIELD = 'ownername'
    REQUIRED_FIELDS = ['email']
    
    
    # class AbstractUser(AbstractBaseUser, PermissionsMixin):
    #     abstract = True
    class Meta():
        db_table = "Owner"

    def __str__(self):
        return self.ownername


