from django.contrib import admin
from .models import Customer, Product, Category, Order, OrderStatusChangeLog

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Customer)
# admin.site.register(Order)
# admin.site.register(OrderStatusChangeLog)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name','id']
    search_fields = ['name']
    fieldsets = (
        (None, {
            "fields": ('name','id'),
               }), 
            )

    



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','email','phone_number','is_active']
    list_filter = ['phone_number','email']
    search_fields = ['phone_number']
    fieldsets = (
        (None, {
            "fields": (
                'name',
                'lastname',
                'email',
                'Phone_number',
                'address',
                'is_active',
                'password',
                
            ),
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','status','name','phone','is_active']
    list_filter = ['status','name','phone']
    search_fields = ['id','name']
    fieldsets = (
        (None, {
            "fields": (
                'product',
                'quentity',
                'status',
                'name',
                'phone',
                'is_active',
                'address',
                'date',
    
            ),
        }),
    )
    

@admin.register(OrderStatusChangeLog)
class OrderStatusChangeLogAdmin(admin.ModelAdmin):
    list_display = ['order','old_status','new_status','changed_at']
    list_filter = ['order']
    search_fields = ['id','order']
    fieldsets = (
        (None, {
            "fields": ('order','old_status','new_status','changed_at'),
               }), 
            )
        
