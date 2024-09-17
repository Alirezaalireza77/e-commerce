from django.db import models
from customer.models import Customer
import factory 
from random import choices
import string



class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = factory.lazy_attribute(lambda o: '{}.{}@gmail.com'.format(o.name,o.lastname).lower())
    phone_number = factory.lazy_attribute(lambda o: "09"+"".join(choices(string.digits, k=7)))
    name = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    password = factory.lazy_attribute(lambda o : "".join(choices(string.ascii_letters + string.digits + "!@#$%^&*", k=10)))