from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    def get_three_last_parent(self):
        parents = [self]
        current_parent = self.parent
        while current_parent is not None and len(parents) < 3:
            parents.append(current_parent)
            current_parent = current_parent.parent
        return parents


        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(
        max_digits=12, decimal_places=0, null=True, blank=True)
    picture = models.ImageField(upload_to='upload/product', null=True, blank=True)
    cast_price = models.DecimalField(
        decimal_places=0, max_digits=12, null=True)
    is_sale = models.BooleanField(default=False)
    star = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

        
    def __str__(self):
        return self.name


