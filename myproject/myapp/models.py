from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emial = models.EmailField(unique=True)
    mobile_number = models.PositiveIntegerField(unique=True)
    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_number = models.CharField(max_length=100,primary_key=True)
    