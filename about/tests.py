from django.test import TestCase, Client
from django.urls import reverse
from django.http import Http404
from .models import About, FAQ


class AboutModelsTest(TestCase):
    def setUp(self):
        About.objects.create(title="Test About Title", content="Test About Content")
        FAQ.objects.create(question="Test FAQ Question", answer="Test FAQ Answer")

    def test_about_model_str(self):
        about = About.objects.get(title="Test About Title")
        self.assertEqual(str(about), "Test About Title")

    def test_faq_model_str(self):
        faq = FAQ.objects.get(question="Test FAQ Question")
        self.assertEqual(str(faq), "Test FAQ Question")

    def test_about_model_ordering(self):
        about_titles = [about.title for about in About.objects.all()]
        self.assertEqual(about_titles, ["Test About Title"])

class AboutViewTests(TestCase):
    def setUp(self):
        self.about = About.objects.create(title='Test About', content='Test content')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer')

    def test_about_page_view(self):
        client = Client()
        url = reverse('about_page')
        response = client.get(url)

        # Assert the expected HTTP status code
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is being used
        self.assertTemplateUsed(response, 'about/about.html')

        # Assert that the about_content and faqs are present in the context
        self.assertIn('about_content', response.context)
        self.assertIn('faqs', response.context)

        # Assert that the about_content and faqs match the data created in the setUp method
        self.assertQuerysetEqual(response.context['about_content'], [repr(self.about)])
        self.assertQuerysetEqual(response.context['faqs'], [repr(self.faq)])

