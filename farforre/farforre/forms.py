from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']
