from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'lastname','email', 'phone_number', 'password', 'address', 'is_staff']