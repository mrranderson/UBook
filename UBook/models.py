from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core import validators
import re

class UBookProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
    cc_type = models.CharField(max_length=20, choices=((1, "Visa"), (2, "Mastercard"), (3, "American Express"), (4, "Discover")), default=1)
    cc_number = models.CharField(max_length=20, blank=True)
    cc_expdate = models.CharField(max_length=10, blank=True)
    cc_ccv = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.user.username

class UBookProfileForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255, validators=[validators.validate_email])
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    state = forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=255)
    cc_type = forms.CharField(max_length=16)
    cc_number = forms.CharField(max_length=20)
    cc_expdate = forms.CharField(max_length=10)
    cc_ccv = forms.CharField(max_length=3)

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not re.match('^[a-zA-Z]*$', data):
            raise forms.ValidationError("Please enter a name containing only alphabetical characters.")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not re.match('^[a-zA-Z]*$', data):
            raise forms.ValidationError("Please enter a name containing only alphabetical characters.")
        return data

    def clean_zipcode(self):
        data = self.cleaned_data['zipcode']
        if not re.match('\d\d\d\d\d(-\d\d\d\d)?', data):
            raise forms.ValidationError("Please enter a valid zipcode in the form of 12345 or 12345-6789.")
        return data
    
    def clean_cc_number(self):
        data = self.cleaned_data['cc_number']
        if not re.match('\d{16}', data):
            raise forms.ValidationError("Please enter a valid credit card number in the form of 0000111122223333.")
        return data

    def clean_cc_expdate(self):
        data = self.cleaned_data['cc_expdate']
        if not re.match('\d\d[/-]\d\d[/-]\d\d\d\d', data):
            raise forms.ValidationError("Please enter a valid expiration date in the form of MM/DD/YYYY or MM-DD-YYYY.")
        return data

    def clean_cc_ccv(self):
        data = self.cleaned_data['cc_ccv']
        if not re.match('\d\d\d', data):
            raise forms.ValidationError("Please enter a valid CCV in the form of 123.")
        return data
