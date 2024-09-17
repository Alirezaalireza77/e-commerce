from order.models import Order, OrderStatusChangeLog
import factory 
from customer.tests.factories import CustomerFactory
from shop.tests.factories import CategoryFactory, ProductFactory
import string
from random import choices


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