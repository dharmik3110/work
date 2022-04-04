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

