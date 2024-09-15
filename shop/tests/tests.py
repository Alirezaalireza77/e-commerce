from typing import Any
from django.test import TestCase
import factory.django
from shop.models import Category, Customer, Product, Order, OrderStatusChangeLog
import factory
from django.core.exceptions import ValidationError
#Create your tests here.

class OrderTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='test')
        product = Product.objects.create(name='product', category=category)
        self.user = Customer.objects.create(name='ali', lastname = 'tohidi', email='admin@gmail.com', phone_number='09121213123', password='1234')
        self.order= Order.objects.create(name=self.user, product=product)
        
   
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

    def test_change_status_log_from_cance(self):
        self.order.change_status('cancel')
        log_entries = OrderStatusChangeLog.objects.filter(order=self.order)
        last_log_entry = log_entries.last()
        self.assertEqual(last_log_entry.old_status, 'new')
        self.assertEqual(last_log_entry.new_status, 'cancel')


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



