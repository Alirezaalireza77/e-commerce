from rest_framework import seralizers
from .models import Cart, CartItem


class CartSerializaer(seralizers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['customer', 'created_at', 'changed_at', 'total_amount']


class CartItemSeralizer(seralizers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'price']