from .models import Category, Product
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'picture', 'cast_price', 'is_sale', 'star']




class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    

    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password']

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return user
        raise serializers.ValidationError('Invalid credentials.')


class LogoutSerializer(serializers.ModelSerializer):
    pass