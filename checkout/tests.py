from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django_countries.fields import Country

from checkout.models import Order, OrderLineItem
from products.models import Product

class CheckoutModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.product = Product.objects.create(name='Test Product', price=10.0, abv="1.1")

    def test_order_creation(self):
        order = Order.objects.create(
            user_profile=None,
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country=Country('US'),
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 4',
            county='Test County',
            original_bag='{}',
            stripe_pid='testpid'
        )

        # Check if order number is generated
        self.assertIsNotNone(order.order_number)

        # Check if order total is zero initially
        self.assertEqual(order.order_total, 0)

        # Check if delivery cost is set to default
        self.assertEqual(order.delivery_cost, 0)

        # Check if grand total is initially zero
        self.assertEqual(order.grand_total, 0)


    def test_line_item_creation(self):
        order = Order.objects.create(
            user_profile=None,
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country=Country('US'),
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 4',
            county='Test County',
            original_bag='{}',
            stripe_pid='testpid'
        )

        line_item = OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
            lineitem_total=self.product.price * 2
        )

        # Check if the line item is associated with the correct order
        self.assertEqual(line_item.order, order)

    def test_order_total_calculation(self):
        order = Order.objects.create(
            user_profile=None,
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country=Country('US'),
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 4',
            county='Test County',
            original_bag='{}',
            stripe_pid='testpid'
        )

        line_item1 = OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
            lineitem_total=self.product.price * 2
        )

        line_item2 = OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=3,
            lineitem_total=self.product.price * 3
        )

        # Check if the order total is calculated correctly
        self.assertEqual(order.order_total, line_item1.lineitem_total + line_item2.lineitem_total)
