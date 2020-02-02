from django import forms
from django.core.validators import RegexValidator
from phone_field import PhoneField
import phone_field


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        help_text="Enter your name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'form-control',
            'id': 'name',
            'type': 'text',
            'required': "required",
            'data - validation - required - message': "Please enter your name."
        })
    )
    email_address = forms.EmailField(
        label='Email Address',
        help_text="Enter your email address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
            'id': 'email',
            'type': 'email',
            'required': "required",
            'data - validation - required - message': "Please enter your email address."
        })
    )
    # cell = PhoneField()
    phone_number = forms.CharField(
        label='Contact number',
        validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
        help_text="Enter your contact number",
        widget=forms.TextInput(attrs={
            'placeholder': 'Contact Number',
            'class': 'form-control',
            'id': 'phone',
            'type': 'tel',
            'required': "required",
            'data - validation - required - message': "Please enter your phone number."
        })
    )
    message = forms.CharField(
        label='Message',
        empty_value='Message',
        widget=forms.Textarea(attrs={
            'placeholder': 'Message',
            'class': 'form-control',
            'id': 'message',
            'rows': '5',
            'required': "required",
            'data - validation - required - message': "Please enter a message."
        })
    )





