from cart.models import Cart, CartItem
from customer.tests.factories import CustomerFactory
from shop.tests.factories import ProductFactory
import factory



class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart
    customer = factory.SubFactory(CustomerFactory)
    total_amount = factory.Faker('random_int', min=0)


class CartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartItem
    cart = factory.SubFactory(CartFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=0, max=100)
    price = factory.lazy_attribute(lambda o: o.product.price)

    