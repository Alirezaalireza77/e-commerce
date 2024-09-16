from django.contrib import admin
from .models import Customer, Product, Category, Order, OrderStatusChangeLog

class ProductCategoryInline(admin.TabularInline):
    model = Product
    fk_name = "category" 
    extra = 1
    fields = ['name','price','star','cast_price']


class OrderProductInline(admin.TabularInline):
    model = Order
    fk_name = "product"
    extra = 1
    fields = ['name','quantity','status','phone','product']
    exclude = ['date','is_active','address']


class OrderChangeInline(admin.TabularInline):
    model = OrderStatusChangeLog
    fk_name = "order"
    extra = 1
    fields = ['old_status','new_status']



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



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','email','phone_number','is_active']
    list_filter = ['phone_number','email']
    search_fields = ['phone_number','id']
    fieldsets = (
        ('Customer', {
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
    search_fields = ['name']
    inlines = [OrderChangeInline]
    fieldsets = (
        ('Order', {
            "fields": (
                'product',
                'quantity',
                'status',
                'name',
                'phone',
                'is_active',
                'address',
    
            ),
        }),
    )
    

# @admin.register(OrderStatusChangeLog)
# class OrderStatusChangeLogAdmin(admin.ModelAdmin):
#     list_display = ['order','old_status','new_status','changed_at']
#     list_filter = ['order']
#     search_fields = ['order','id']
#     fieldsets = (
#         ('LogChanging', {
#             "fields": ('order',
#                        'old_status',
#                        'new_status',
#                        'changed_at',
#                     ),
#                }), 
#             )
        
