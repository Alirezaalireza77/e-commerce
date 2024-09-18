from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Product
from customer.models import Customer
from datetime import datetime


# Create your models here.
class Order(models.Model):
    status_choice = [
        ('new', 'New'),
        ('paid', 'Paid'),
        ('sent', 'Sent'),
        ('cancel', 'Cancel'),
    ]

    valid_status_changing = {
        'new': ['paid', 'cancel'],
        'paid': ['sent'],
        'sent': [],
        'cancel': [],
    }

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    status = models.CharField(
        max_length=20, choices=status_choice, default='new')
    name = models.ForeignKey(Customer, on_delete=models.PROTECT)
    address = models.TextField(max_length=100, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'


    def clean(self):
        super().clean()
        if self.quantity < 1:
            raise ValidationError('quentities of order must be 1 atleast.')
        if not self.phone.isdigit():
            raise ValidationError('phone number must contain only number.')
        if not self.phone.startswith('09'):
            raise ValidationError('phone number must be started with "09".')
        

    @transaction.atomic
    def change_status(self, new_status):
        current_status = self.status
        if new_status not in self.valid_status_changing.get(current_status, []):
            raise ValidationError(f"Invalid status and you cannot change status from {
                                  current_status} to {new_status}.")
        self.status = new_status
        self.save()

        OrderStatusChangeLog.objects.create(
            order=self,
            old_status=current_status,
            new_status=new_status,
            changed_at=datetime.now()
        )

    def __str__(self):
        return f' order:{self.product} - status: {self.status}'


class OrderStatusChangeLog(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_at = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f' log:{self.old_status} changed to {self.new_status} at {self.changed_at}'
