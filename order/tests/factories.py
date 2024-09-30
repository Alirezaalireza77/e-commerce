from order.models import Order, OrderStatusChangeLog
import factory 
from django.contrib.auth.models import User
from shop.tests.factories import ProductFactory
import string
from random import choices



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.Faker('password')


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)
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