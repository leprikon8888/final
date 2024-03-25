from django.test import TestCase, Client
from home.forms import FormContactForm

class FormContactFormTestCase(TestCase):
    def test_form_contact_form_valid(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'message': 'Test message'
        }
        form = FormContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_contact_form_invalid(self):
        form_data = {
            'name': '',
            'email': 'invalid-email',
            'phone': '',
            'message': ''
        }
        form = FormContactForm(data=form_data)
        self.assertFalse(form.is_valid())