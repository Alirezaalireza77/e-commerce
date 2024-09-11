from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError   


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(blank=False, max_length=100)
    phone_number = models.CharField(blank=False, max_length=13)
    password = models.CharField(max_length=128)
    address = models.TextField(max_length=10, default="", null=True, blank=True)

    def __str__(self):
        return f'{self.name}{self.lastname}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True)
    picture = models.ImageField(upload_to='upload/product', null=True)
    cast_price = models.DecimalField(decimal_places=0, max_digits=12, null=True)
    is_sale = models.BooleanField(default=False)
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name


class Order(models.Model):
    status_choice=[
       ('new', 'New'),
       ('paid','Paid'),
       ('sent','Sent'),
       ('cancel','Cancel'),
    ]
    
    valid_status_changing ={
        'new' :['paid', 'cancel'],
        'paid':['sent'],
        'sent' :[],
        'cancel' : [],
    }

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,)
    status = models.CharField(max_length=20, choices=status_choice, default='new')
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField(max_length=1000, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    date = models.DateField(auto_now_add=True)

    
    def change_status(self, new_status):
        current_status = self.status
        if self.status not in self.valid_status_changing:
            raise ValidationError(f"Invalid status and you cannot change status from {current_status} to next status.")

        self.status = new_status
        self.save()
    
    #def change_status(self, new_status):
    #    if self.status == 'new':
    #       if new_status in ['paid', 'cancel']:
    #            self.status = new_status
    #        else:
    #            raise ValidationError('Invalid changing status from new.')
    #    elif self.status == 'paid':
    #        if self.status == 'sent':
    #            self.status = new_status
    #        else:
    #            raise ValidationError('Invalid changing status from paid level.')
    #    elif self.status =='sent':
    #        raise ValidationError('your order sent to you and you cannot change status position.')
    #    elif self.status =='cancel':
    #        raise ValidationError('you cannot change status from cancel.')
    #    else:
    #        raise ValidationError('unknown status.')
    #    self.save()

    
    def __str__(self):
        return f' order:{self.product} - status: {self.status}'
    

