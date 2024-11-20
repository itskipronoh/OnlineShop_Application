# from django.db import forms
from django import forms


from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Phone'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'age': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Age'}),
            'admNo': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Admission Number'}),

        }

        Customer.model = Customer
