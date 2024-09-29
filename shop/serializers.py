from .models import Category, Product
from rest_framework import serializers
from django.contrib.auth.models import User


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'picture', 'cast_price', 'is_sale', 'star']




class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

    
