from rest_framework import serializers
from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'created_at', 'cart_key', 'changed_at', 'total_amount']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'price']