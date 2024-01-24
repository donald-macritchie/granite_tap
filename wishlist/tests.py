from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from wishlist.models import Wishlist


class WishlistModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            brewery='Test Brewery',
            abv=5.0,
            description='Test Description',
            volume='Test Volume',
            price=20.0,
        )

    def test_wishlist_creation(self):
        wishlist = Wishlist.objects.create(user=self.user)
        wishlist.products.add(self.product)

        # checks number of wishlist items
        self.assertEqual(Wishlist.objects.count(), 1)
        # checks if expected user
        self.assertEqual(wishlist.user, self.user)
        # checks if added product is in the wishlist
        self.assertTrue(wishlist.products.filter(pk=self.product.pk).exists())
