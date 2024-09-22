from django.db import models
from customer.models import Customer
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT)
    cart_key = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Changed_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'


    def calculate_total_price(self):
        total_price = 0
        total_quantity = 0
        cart_items = self.cartitem_set.all()

        for product in cart_items:
            total_price += product.product.price * product.quantity
            total_quantity += product.quantity

        self.total_amount = total_price
        self.save()
        return self.total_amount, total_price


    def __str__(self):
        return f'{self.customer}'
    


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=0)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'


    def __str__(self):
        return f'{self.quantity}'