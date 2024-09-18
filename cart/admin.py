from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.

class CartItemCartInline(admin.TabularInline):
    model = CartItem
    fk_name = "cart"
    extra = 1
    fields = ['cart','product', 'quantity', 'price']




@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer','created_at','total_amount']
    search_fields = ['customer']
    list_filter = ['id', 'customer']
    inlines = [CartItemCartInline]
    fieldsets = (
        ('Cart', {
            "fields": (
                'customer',
                'total_amount',
            ),
        }),
    )
    
    
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','product','quantity','price']
    search_fields = ['product', 'cart']
    list_filter = ['id', 'product']
    fieldsets = (
        ('CartItem', {
            "fields": (
                'cart',
                'product',
                'price',
            ),
        }),
    )
    