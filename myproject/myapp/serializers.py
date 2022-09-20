from rest_framework import serializers
from .models import User, Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fileds = ['first_name','last_name','email','phone_number']
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fileds = ['user','profile_number']