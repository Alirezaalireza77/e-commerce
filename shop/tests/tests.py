from typing import Any
from django.test import TestCase
import factory.django
import factory
from django.core.exceptions import ValidationError
from .factories import CategoryFactory, CustomerFactory, ProductFactory, OrderFactory, OrderStatusChangeLogFactory

class CategoryTest(TestCase):

    def test_get_three_last_parent(self):
        top_category = CategoryFactory(name='laptop')
        second_category = CategoryFactory(parent=top_category)
        third_category = CategoryFactory(parent=second_category)
        fourth_category = CategoryFactory(parent=third_category)
        fifth_category = CategoryFactory(parent=fourth_category)

        parents = fifth_category.get_three_last_parent()
        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[0], fifth_category)
        self.assertEqual(parents[1], fourth_category)
        self.assertEqual(parents[2], third_category)


    def test_get_three_last_parent_less_than_three_parents(self):
        top_category = CategoryFactory()
        second_category = CategoryFactory(parent=top_category)
        third_category = CategoryFactory(parent=second_category)

        parents = third_category.get_three_last_parent()
        self.assertEqual(len(parents), 3)
        self.assertEqual(parents[1], second_category)
        self.assertEqual(parents[2], top_category)

    def test_get_three_last_parent_no_parent(self):
        category = CategoryFactory()
        parents = category.get_three_last_parent()
        self.assertEqual(len(parents), 1)


class CustomerTestCase(TestCase):
    def test_check_short_password(self):
        customer = CustomerFactory()
        customer.password = 'Azura12'
        with self.assertRaises(ValidationError) as context:
            customer.clean()
        self.assertEqual(str(context.exception), "['password must has 8 charactor atlist.']")  

    
    def test_check_just_number_for_password(self):
        customer = CustomerFactory()
        customer.password = '12345678'
        with self.assertRaises(ValidationError) as context:
            customer.clean()
        self.assertEqual(str(context.exception), "['password must contains atleast one charactor.']")


    def test_check_only_letter_password(self):
        customer = CustomerFactory()
        customer.password = 'swertfef'
        with self.assertRaises(ValidationError) as context:
            customer.clean()
        self.assertEqual(str(context.exception), "['password must has atleast one number.']")


    def test_check_only_letter_without_uppercase(self):
        customer = CustomerFactory()
        customer.password = 'swkdkwd2'
        with self.assertRaises(ValidationError) as context:
            customer.clean()
        self.assertEqual(str(context.exception), "['password must contains atleast one UPERCASE charactor.']")


    def test_check_password_without_symbol(self):
        customer = CustomerFactory()
        customer.password = 'swe23SWr'
        with self.assertRaises(ValidationError) as context:
            customer.clean()
        self.assertEqual(str(context.exception), "['password must has atleast one symbol.']")


    def test_valid_password(self):
        customer = CustomerFactory()
        customer.password = 'sw123Ad@'
        customer.clean()


class OrderTestCase(TestCase):
    def setUp(self):
        self.order = OrderFactory()

    def test_change_status_valid(self):
        order = OrderFactory()
        order.change_status('paid')
        self.assertEqual(order.status, 'paid')
        log_entry = OrderStatusChangeLogFactory(order=order, old_status='new', new_status='paid')
        self.assertEqual(log_entry.old_status, 'new')
        self.assertEqual(log_entry.new_status, 'paid')


    def test_change_status_invalid(self):
        order = OrderFactory()
        with self.assertRaises(ValidationError) as context:
            order.change_status('sent')
        self.assertEqual(str(context.exception), "['Invalid status and you cannot change status from new to sent.']")   
        self.assertEqual(order.status, 'new')

    def test_change_status_log_from_cancel(self):
        order = OrderFactory()
        order.change_status('cancel')
        log_entries = OrderStatusChangeLogFactory(order=order, old_status='new', new_status= 'cancel')
        last_log_entry = log_entries
        self.assertEqual(last_log_entry.old_status, 'new')
        self.assertEqual(last_log_entry.new_status, 'cancel')


    def test_change_status_log(self):
        order = OrderFactory()
        order.change_status('paid')
        log_entries = OrderStatusChangeLogFactory(order=order, old_status='new', new_status='paid')
        last_log_entry = log_entries
        self.assertEqual(last_log_entry.old_status, 'new')
        self.assertEqual(last_log_entry.new_status, 'paid')

    
    def test_change_status_log_from_paid(self):
        order = OrderFactory()
        order.status = 'paid'
        order.change_status('sent')
        log_entries = OrderStatusChangeLogFactory(order=order, old_status='paid', new_status='sent')
        last_log_entry = log_entries
        self.assertEqual(last_log_entry.old_status, 'paid')
        self.assertEqual(last_log_entry.new_status, 'sent')


    def test_phone_number_invalid(self):
            order = OrderFactory()
            order.phone = '08137327372'
            with self.assertRaises(ValidationError) as context:
                order.clean()
                self.assertEqual(str(context.exception),"['phone number must be started with \"09\"']")

    def test_phone_not_number(self):
        order = OrderFactory()
        order.phone = '09ft7876845'
        with self.assertRaises(ValidationError) as context:
            order.clean()
            self.assertEqual(str(context.exception), "['phone number must contain only number.']")


    def test_phone_number_valid(self):
        order = OrderFactory()
        order.quantity = 1
        order.phone = '09121212121'
        order.clean()
        
        

    def test_number_of_quantity_invalid(self):
        order = OrderFactory()
        order.quantity = 0
        with self.assertRaises(ValidationError) as context:
            order.clean()
            self.assertEqual(str(context.exception), "['quentities of order must be 1 atleast.']")


    def test_quantity_valid(self):
        order = OrderFactory()
        order.quantity = 1
        order.phone = '09121212122'
        order.clean()


