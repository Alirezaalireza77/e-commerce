import factory  
from shop.models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)
    price = factory.Faker('random_int', min=1, max=100)
    description = factory.Faker('text')



    
