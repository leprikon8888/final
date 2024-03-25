from django.test import TestCase, Client
from home.models import Service, ServiceBlock, AboutBlock, AboutUnit, Team, Client, Shapka, BrandName, BrandFace, PortfolioBlock, Portfolio, ContactBlock, Niz, FormContact

class ModelTestCase(TestCase):
    def test_service_block_str(self):
        service_block = ServiceBlock.objects.create(name='Test Service Block', description='Test description')
        self.assertEqual(str(service_block), 'Test Service Block')

    def test_service_str(self):
        service_block = ServiceBlock.objects.create(name='Test Service Block', description='Test description')
        service = Service.objects.create(service_block=service_block, name='Test Service', slug='test-service', position=1, description='Test description', icon='test-icon')
        self.assertEqual(str(service), 'Test Service')

    # Добавьте тесты для других моделей

    def test_form_contact_str(self):
        form_contact = FormContact.objects.create(name='John Doe', email='john@example.com', phone='1234567890',
                                                  message='Test message')
        self.assertEqual(str(form_contact), 'John Doe (john@example.com)')