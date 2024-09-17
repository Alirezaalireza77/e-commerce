from django.test import TestCase
from .factories import CustomerFactory
from django.core.exceptions import ValidationError
# Create your tests here.

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
