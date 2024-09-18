from .models import Category, Product
from rest_framework import serializers


class CategorySeializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'picture', 'cast_price', 'is_sale', 'star']