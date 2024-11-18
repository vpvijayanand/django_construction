# masters/forms.py
from django import forms
from .models import EmployeeType, VendorType ,BrandType,EmployeeRolles

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']

class VendorTypeForm(forms.ModelForm):
    class Meta:
        model = VendorType
        fields = ['name']

class BrandTypeForm(forms.ModelForm):
    class Meta:
        model = BrandType
        fields = ['name']
        
class EmployeeRollesForm(forms.ModelForm):
    class Meta:
        model = EmployeeRolles
        fields = ['name']