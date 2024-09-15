from typing import Any
from django.test import TestCase
import factory.django
from shop.models import Category, Customer, Product, Order, OrderStatusChangeLog
import factory
from django.core.exceptions import ValidationError


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'test'



class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'product'
    category = factory.SubFactory(CategoryFactory)



class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    email = 'admin@gmail.com'
    phone_number = '09121212121'
    

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    name = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)



class OrderTestCase(TestCase):
    def setUp(self):
        self.order = OrderFactory()


    def test_change_status_valid(self):
        self.order.change_status('paid')
        self.assertEqual(self.order.status, 'paid')
        log_entry = OrderStatusChangeLog.objects.get(order=self.order)
        self.assertEqual(log_entry.old_status, 'new')
        self.assertEqual(log_entry.new_status, 'paid')


    def test_change_status_invalid(self):
        with self.assertRaises(ValidationError) as context:
            self.order.change_status('sent')

        self.assertEqual(str(context.exception), "['Invalid status and you cannot change status from new to sent.']")
        self.assertEqual(self.order.status, 'new')


    def test_change_status_log_cancel(self):
        self.order.change_status('cancel')
        log_entries = OrderStatusChangeLog.objects.filter(order=self.order)
        last_log_entry = log_entries.last()
        self.assertEqual(last_log_entry.old_status, 'new')
        self.assertEqual(last_log_entry.new_status, 'cancel')

    
    def test_change_status_log_from_cancel(self):
        self.order.status = 'cancel'
        with self.assertRaises(ValidationError) as context:
            self.order.change_status('paid')

        self.assertEqual(str(context.exception), "['Invalid status and you cannot change status from cancel to paid.']")
        self.assertEqual(self.order.status, 'cancel')


    def test_change_status_invalid_from_unknown_status(self):
        with self.assertRaises(ValidationError) as context:
            self.order.change_status('unknown_status')
            self.assertEqual(str(context.exception), "['Invalid status and you cannot change status from new to unknown_status.']" )
            self.assertEqual('new')


    def test_change_status_log(self):
        self.order.change_status('paid')
        log_entries = OrderStatusChangeLog.objects.filter(order=self.order)
        last_log_entry = log_entries.last()
        self.assertEqual(last_log_entry.old_status, 'new')
        self.assertEqual(last_log_entry.new_status, 'paid')


    def test_change_status_log_from_paid(self):
        self.order.status = 'paid'
        self.order.change_status('sent')
        log_entries = OrderStatusChangeLog.objects.filter(order=self.order)
        last_log_entry = log_entries.last()
        self.assertEqual(last_log_entry.old_status, 'paid')
        self.assertEqual(last_log_entry.new_status, 'sent')

