from django.contrib import admin
from .models import Customer, Product, Category, Order, OrderStatusChangeLog

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderStatusChangeLog)