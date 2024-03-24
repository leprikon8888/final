from django import forms
from .models import FormContact


class FormContactForm(forms.ModelForm):
    class Meta:
        model = FormContact
        fields = ('name', 'email', 'phone', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                                           'required': True }),
            'email': forms.EmailInput(attrs={'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                                              'required': True}),
            'phone': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Your Phone", 'required': True}),
            'message': forms.Textarea(attrs={'class': "form-control", 'id': "message", 'placeholder': "Your Message",
                                             'required': True})
        }
