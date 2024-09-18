from django.test import TestCase
from cart.models import Cart, CartItem
from .factories import CartFactory, CartItemFactory, ProductFactory

# Create your tests here.

class CartTestCase(TestCase):
    def setUp(self):
        self.cart = CartFactory()
        self.product1 = ProductFactory(price=100)
        self.product2 = ProductFactory(price=200)
        
        CartItemFactory(cart=self.cart, product=self.product1, quantity=2)
        CartItemFactory(cart=self.cart, product=self.product2, quantity=1)


    def test_cart_total_price_calculation(self):
        total_amount, calculated_total_price = self.cart.calculate_total_price()
        total_price = (self.product1.price * 2) + (self.product2.price * 1)
        
        self.assertEqual(total_amount, total_price)
        self.assertEqual(calculated_total_price, total_price)


    def test_cart_string_representation(self):
        self.assertEqual(str(self.cart), str(self.cart.customer))
    

    def test_cart_creation(self):
        self.assertEqual(Cart.objects.count(), 1)


    def test_cartitem_string_representation(self):
        cart_item = CartItemFactory(cart=self.cart)
        self.assertEqual(str(cart_item), str(cart_item.quantity))