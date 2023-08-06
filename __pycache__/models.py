from django.db import models
from django.contrib.auth.models import User

from django.db import models

# Define a data model for storing information like name, age, sex, height, and weight.
class Patient(models.Model):
   hospital_name = models.CharField(max_length=100, default='ABC Hospital')
   address = models.CharField(max_length=200, default='Default Address')
   speciality = models.CharField(max_length=100,default='Speciality type')
   contact_number = models.CharField(max_length=20,  default='123456789')
   short_intro = models.TextField(default='Short intro.')
   email = models.EmailField(default='example@example.com')
 
   
   def __str__(self):
        return self.name
