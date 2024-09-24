from cart.models import Cart, CartItem
from shop.tests.factories import ProductFactory
import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class CartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cart
    user = factory.SubFactory(UserFactory)
    total_amount = factory.Faker('random_int', min=0)


class CartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartItem
    cart = factory.SubFactory(CartFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.Faker('random_int', min=0, max=100)
    price = factory.lazy_attribute(lambda o: o.product.price)

    