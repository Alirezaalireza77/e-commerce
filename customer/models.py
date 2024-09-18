from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(blank=False, max_length=100)
    phone_number = models.CharField(blank=False, max_length=11)
    password = models.CharField(max_length=128)
    address = models.TextField(
        max_length=100,
        default="",
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


    def clean(self):
        super().clean()
        if len(self.password) < 8:
            raise ValidationError('password must has 8 charactor atlist.')
        if not re.search(r"[0-9]", self.password):
            raise ValidationError('password must has atleast one number.')
        if not re.search(r"[a-z]", self.password):
            raise ValidationError('password must contains atleast one charactor.')
        if not re.search(r"[A-Z]", self.password):
            raise ValidationError('password must contains atleast one UPERCASE charactor.')
        if not re.search(r"[!|@|#|$|%|&|*]", self.password):
            raise ValidationError('password must has atleast one symbol.')

    def __str__(self):
        return f'{self.name} {self.lastname}'

