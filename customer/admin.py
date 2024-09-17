from django.contrib import admin
from .models import Customer


# Register your models here.
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
                'phone_number',
                'address',
                'is_active',
                'password',
                
            ),
        }),
    )


