
from django.test import TestCase

from .models import *


# Create your tests here.
class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="ali",lastname="razavi")
        Customer.objects.create(name="hossein", lastname="vahidi")

    def test_customer_name(self):
        customer1 = Customer.objects.get(name="ali")
        customer2 = Customer.objects.get(name="hossein")

        self.assertEqual(customer1.name, 'ali')
        self.assertEqual(customer2.name, "hossein")

        


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="appliance")
        Category.objects.create(name="washers")

    def test_category_name(self):
        category1 = Category.objects.get(name="appliance")
        category2 = Category.objects.get(name="washers")

        self.assertEqual(category1.name, "appliance")
        self.assertEqual(category2.name, "washers")


class ProductTestCase(TestCase):
    def setUp(self):
        category= Category.objects.create(name="test")
        Product.objects.create(name="box", category=category)
        Product.objects.create(name="paper", category=category)
        self.category= category


    def test_product_name(self):
        product1 = Product.objects.get(name="box", category=self.category)
        product2 = Product.objects.get(name="paper", category=self.category)

        self.assertEqual(product1.name, "box")
        self.assertEqual(product2.name, "paper")


class OrderTestCase(TestCase):
    def setUp(self):
        
        category = Category.objects.create(name='test')
        p1=Product.objects.create(name='p1', category=category)
        c1=Customer.objects.create(name='ali', lastname='kiani', email='ali@gmail.com', phone_number='09016536128', password='123')
        Order.objects.create(name=c1, product=p1)
        self.c1= c1
        # Order.objects.create(name="sabad")

    def test_order_name(self):
        order1= Order.objects.get(name=self.c1)
        # order2 = Order.objects.get(name="sabad")

        self.assertEqual(order1.name, self.c1)
        # self.assertEqual(order2.name, "sabad")



