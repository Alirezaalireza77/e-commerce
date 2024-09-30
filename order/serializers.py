from .models import Order, OrderStatusChangeLog
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'status', 'user', 'address', 'phone', 'date', 'is_active']
        read_only_fields = ['date', 'status', 'user']


    def validate_phone(self, value):
        if not value.startswith('09') and not value.isdigit():
            raise serializers.ValidationError('phone number must contain digits and starts with 09.')
        return value
    
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError('oder quantity must be atleast 1.')
        return value


    def create(self, validated_data):
        user = self.context['request'].user
        order = Order.objects.create(user=user, **validated_data)
        return order
    

    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        if 'status' in validated_data:
            instance.change_status(new_status)
        return super().update(instance, validated_data)


class OrderStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusChangeLog
        fields = ['order', 'old_status', 'new_status', 'changed_at']