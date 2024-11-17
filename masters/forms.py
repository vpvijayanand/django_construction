# masters/forms.py
from django import forms
from .models import EmployeeType, VendorType

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']

class VendorTypeForm(forms.ModelForm):
    class Meta:
        model = VendorType
        fields = ['name']
