from dataclasses import fields
import imp
from django import forms
from .models import Contacts
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    ph_num = PhoneNumberField()

    class Meta:
        model = Contacts
        fields = ["first_name", "last_name", "ph_num"]