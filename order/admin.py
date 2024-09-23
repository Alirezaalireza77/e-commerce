from django.contrib import admin
from .models import Order, OrderStatusChangeLog
# Register your models here.

class OrderChangeInline(admin.TabularInline):
    model = OrderStatusChangeLog
    fk_name = "order"
    extra = 1
    fields = ['old_status','new_status']


class OrderProductInline(admin.TabularInline):
    model = Order
    fk_name = "product"
    extra = 1
    fields = ['name','quantity','status','phone','product']
    exclude = ['date','is_active','address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','status','user','phone','is_active']
    list_filter = ['status','user','phone']
    search_fields = ['name']
    inlines = [OrderChangeInline]
    fieldsets = (
        ('Order', {
            "fields": (
                'product',
                'quantity',
                'status',
                'user',
                'phone',
                'is_active',
                'address',
    
            ),
        }),
    )
    

@admin.register(OrderStatusChangeLog)
class OrderStatusChangeLogAdmin(admin.ModelAdmin):
    list_display = ['order','old_status','new_status','changed_at']
    list_filter = ['order']
    search_fields = ['order','id']
    fieldsets = (
        ('LogChanging', {
            "fields": ('order',
                       'old_status',
                       'new_status',
                    ),
               }), 
            )
        
