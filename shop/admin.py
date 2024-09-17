from django.contrib import admin
from .models import Product, Category
from order.models import Order, OrderStatusChangeLog
from order.admin import OrderProductInline

class ProductCategoryInline(admin.TabularInline):
    model = Product
    fk_name = "category" 
    extra = 1
    fields = ['name','price','star','cast_price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name','id']
    search_fields = ['name']
    inlines = [ProductCategoryInline]
    fieldsets = (
        ('Category', {
            "fields": ('name',),
               }), 
            )

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_sale']
    list_filter = ['category', 'is_sale'] 
    search_fields = ['name','id'] 
    inlines = [OrderProductInline]
    fieldsets = (
        ('Product', {
            "fields": (
                'name',
                'description',
                'category',
                'price',
                'cast_price',  
                'is_sale',
                'star', 
            ),
        }),
    )

