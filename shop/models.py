from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(blank=False,max_length=100)
    phone_number = models.CharField(blank=False, max_length=13)
    password = models.CharField(max_length=128)
    address = models.TextField(max_length=10, default="", null=True, blank=True)

    def __str__(self):
        return f'{self.name}{self.lastname}'
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True,default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=Category)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True, default='')
    picture = models.ImageField(upload_to='upload/product')
    cast_price = models.DecimalField(decimal_places=0, max_digits=12, null=True, default='')
    is_sale = models.BooleanField(default=False)
    star = models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return self.name
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,)
    status = models.BooleanField(default=True)
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(max_length=1000,blank=False)
    phone = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.product