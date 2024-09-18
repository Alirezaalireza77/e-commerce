from .models import Order, OrderStatusChangeLog
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'status', 'name', 'address', 'phone', 'date', 'is_active']


class OrderStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusChangeLog
        fields = ['order', 'old_status', 'new_status', 'changed_at']