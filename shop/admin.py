from django.contrib import admin
from .models import Customer, Product, Category, Order

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
