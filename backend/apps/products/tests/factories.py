import factory

from apps.products.models import Brand
from apps.products.models import Category
from apps.products.models import Product


class BrandFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    country = factory.Sequence(lambda i: f'Company-{i}')
    parent_brand = None

    class Meta:
        model = Brand


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    title = factory.Faker('name')
    model_year = 2000
    price = 1000
    available = True

    class Meta:
        model = Product
