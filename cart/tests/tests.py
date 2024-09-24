from django.test import TestCase
from cart.models import Cart, CartItem
from .factories import CartFactory, CartItemFactory, ProductFactory, UserFactory
from cart.serializers import CartItemSerializer, CartSerializer

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


    def test_cart_creation(self):
        self.assertEqual(Cart.objects.count(), 1)


    def test_cartitem_string_representation(self):
        cart_item = CartItemFactory(cart=self.cart)
        self.assertEqual(str(cart_item), str(cart_item.quantity))



class CartItemSerializerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.cart = CartFactory(user=self.user)
        self.product = ProductFactory()


    def test_add_item(self):
        serializer_data = {
            'cart': self.cart.id,
            'product': self.product.id,
            'quantity': 2,
        }

        serializer = CartItemSerializer(data=serializer_data)
        self.assertTrue(serializer.is_valid())
        serializer.add_item(serializer.validated_data, serializer.errors)

        cart_item = CartItem.objects.get(cart=self.cart, product=self.product)
        self.assertEqual(cart_item.quantity, 2)