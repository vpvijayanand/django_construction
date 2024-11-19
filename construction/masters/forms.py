# masters/forms.py
from django import forms
from .models import EmployeeType, VendorType ,BrandType,EmployeeRolles,Iteam

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

class IteamForm(forms.ModelForm):
    class Meta:
        model = Iteam
        fields = ['name', 'brand']  # Include 'brand' to select an associated brand
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Item Name'}),
            'brand': forms.Select(attrs={'class': 'form-control'})
        }
        
class EmployeeRollesForm(forms.ModelForm):
    class Meta:
        model = EmployeeRolles
        fields = ['name']