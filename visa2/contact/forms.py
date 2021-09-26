from django import forms
from django.forms import widgets
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        labels= {'name':'Full Name'}
        widgets= {
        'name':forms.TextInput(attrs={'class':'form-control'}),              
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }   