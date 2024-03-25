from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.http import HttpResponseRedirect
from home.models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, PortfolioBlock, Portfolio, ContactBlock, Niz
from home.forms import FormContactForm
from home.views import MainPageView

class MainPageViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.main_page_url = reverse('home:main_page')

    def test_main_page_view(self):
        request = self.factory.get(self.main_page_url)
        response = MainPageView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('index.html', response.template_name)

    def test_main_page_context(self):
        request = self.factory.get(self.main_page_url)
        response = MainPageView.as_view()(request)
        self.assertIsInstance(response.context_data['form_contact'], FormContactForm)
        self.assertTrue('service_block' in response.context_data)
        self.assertTrue('services' in response.context_data)
        # Добавьте проверки для других контекстных переменных

    def test_main_page_post(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Test message'
        }
        request = self.factory.post(self.main_page_url, data=form_data)
        response = MainPageView.as_view()(request)
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, self.main_page_url)