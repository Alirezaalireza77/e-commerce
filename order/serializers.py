from .models import Order, OrderStatusChangeLog
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['date', 'is_active','id', 'user', 'status']


    def validate_phone(self, value):
        if not value.startswith('09') or not value.isdigit():
            raise serializers.ValidationError('phone number must starts with "09" and phone number must contains only digits.')
        return value
    

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError('quantity of order must be atleast 1.')
        return value
    
    def validate_status(self, value):
        instance = self.instance
        if instance:
            current_status = instance.status
            if value not in instance.valid_status_changing.get(current_status, []):
                raise serializers.ValidationError(f"Cannot change status from {current_status} to {value}.")
        return value


    def update(self, instance, validated_data):
        new_status = validated_data.get('status', instance.status)
        if new_status:
            if new_status != instance.status:
                instance.change_status(new_status)
        return super().update(instance, validated_data)
    


class OrderStatusChangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusChangeLog
        fields = ['order', 'old_status', 'new_status', 'changed_at']