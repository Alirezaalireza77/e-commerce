from typing import Any
from django.test import TestCase
import factory
from shop.models import Category, Customer, Product, Order, OrderStatusChangeLog
from django.core.exceptions import ValidationError
from random import choices
import string


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')



class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)
    price = factory.Faker('random_int', min=1, max=100)
    description = factory.Faker('text')



class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = factory.Faker('email')
    phone_number = factory.lazy_attribute(lambda o: "09"+"".join(choices(string.digits, k=7)))
    name = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    password = factory.Faker('password')
    

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    name = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)
    phone = factory.lazy_attribute(lambda o: "09"+"".join(choices(string.digits, k=7)))
    quantity = factory.Faker('random_int', min=1, max=100)
    address = factory.Faker('address')

class OrderStatusChangeLogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderStatusChangeLog

    order = factory.SubFactory(OrderFactory)
    old_status = factory.Faker('random_element', elements=['new','cancel','paid','sent'])
    new_status = factory.Faker('random_element', elements=['new','cancel','paid','sent'])