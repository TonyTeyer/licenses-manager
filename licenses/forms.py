from django.forms import ModelForm
from .models import Licenses
from django import forms

class LicensesForm(ModelForm):
    class Meta:
        model = Licenses
        fields = [
            'companyname',
            'username',
            'jobtitle',
            'email',
            'softwareusername',
            'expirationdate',
            'version',
        ]
        labels = {
            'companyname': 'Company Name',
            'username': 'User Name',
            'jobtitle': 'Job Title',
            'email': 'E-mail',
            'softwareusername': 'Software User Name',
            'expirationdate': 'Expiration Date',
            'version': 'Software Version',
        }
        widgets = {
            
            'companyname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'jobtitle': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'softwareusername': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'expirationdate': forms.DateInput(attrs={
                "type": 'date',
                'class': 'form-control'
            }),
            'version': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }