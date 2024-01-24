from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product


class BagViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            price=10.0,
            abv="1.1"
            )

    def test_view_bag(self):
        client = Client()
        url = reverse('view_bag')
        response = client.get(url)

        # Assert the expected HTTP status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        url = reverse('add_to_bag', args=[self.product.id])
        response = self.client.post(
            url,
            {
                'quantity': 2,
                'redirect_url': reverse('view_bag')
            }
        )

        # Assert the expected HTTP status code
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to view_bag
        response = self.client.get(response.url)

        # Assert that the success message is present in the messages
        messages = [m.message for m in list(response.context['messages'])]
        self.assertIn(f'Added {self.product.name} to your bag', messages)

    def test_adjust_bag_remove_product(self):
        product = self.product
        self.client.post(reverse(
            'add_to_bag',
            args=[product.id]),
            {'quantity': 1, 'redirect_url': reverse('view_bag')}
        )
        item_id = str(product.id)
        response = self.client.post(reverse(
            'adjust_bag', args=[item_id]), {'quantity': 0}
        )
        bag = response.client.session.get('bag', {})

        # Assert that the product is removed from the bag
        self.assertNotIn(item_id, bag)

    def test_remove_from_bag(self):
        self.client.post(reverse(
            'add_to_bag',
            args=[self.product.id]),
            {'quantity': 1, 'redirect_url': reverse('view_bag')}
        )
        item_id = str(self.product.id)
        response = self.client.post(reverse('remove_from_bag', args=[item_id]))
        self.assertEqual(response.status_code, 200)

        # Check that the product is removed from the bag
        bag = self.client.session.get('bag', {})
        self.assertNotIn(item_id, bag)

        # Check the success message
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(f'Removed {self.product.name} from your bag', messages)
