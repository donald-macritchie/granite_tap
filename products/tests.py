from django.test import TestCase
from .models import Category, RelatedProduct, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', friendly_name='Friendly Category')

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')


class RelatedProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            brewery='Test Brewery',
            abv=5.0,
            description='Test Description',
            volume='Test Volume',
            price=20.0,
        )
        self.related_product = RelatedProduct.objects.create(product=self.product)

    def test_related_product_str_method(self):
        expected_str = f'Related product for {self.product.name}'
        self.assertEqual(str(self.related_product), expected_str)

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            category=self.category,
            sku='TestSKU123',
            name='Test Product',
            brewery='Test Brewery',
            abv=5.0,
            description='Test Description',
            volume='Test Volume',
            price=20.0,
        )

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'Test Product')
