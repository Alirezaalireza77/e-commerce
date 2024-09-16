from .models import *
from factory import DjangoModelFactory, Faker, factory
import factory


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test'

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = 'product'
    category = factory.SubFactory(CategoryFactory)

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = Faker('name')
    lastname = Faker('lastname')
    email = Faker('email')
    phone_number = Faker('phone_number')
    password = Faker('password')
    

class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order

    name = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)

