# masters/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from .models import EmployeeType, VendorType
from .forms import EmployeeTypeForm, VendorTypeForm
from django import forms
from django.http import JsonResponse


# EmployeeType Views
"""
class EmployeeTypeListView(ListView):
    model = EmployeeType
    template_name = 'masters/employee_type_list.html'
    context_object_name = 'employee_types'

class EmployeeTypeCreateView(CreateView):
    model = EmployeeType
    form_class = EmployeeTypeForm
    template_name = 'masters/employee_type_form.html'
    success_url = reverse_lazy('employee_type_list')

class EmployeeTypeUpdateView(UpdateView):
    model = EmployeeType
    form_class = EmployeeTypeForm
    template_name = 'masters/employee_type_form.html'
    success_url = reverse_lazy('employee_type_list')

class EmployeeTypeDeleteView(DeleteView):
    model = EmployeeType
    template_name = 'masters/employee_type_delete.html'
    success_url = reverse_lazy('employee_type_list')

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Employee Type'}),
        }
"""
def employee_type_list(request):
    employee_types = EmployeeType.objects.all()
    return render(request, 'masters/employee_type_list.html', {'employee_types': employee_types})

def employee_type_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employee_type = EmployeeType.objects.create(name=name)
        return JsonResponse({'id': employee_type.id, 'name': employee_type.name, 'created_at': employee_type.created_at, 'updated_at': employee_type.updated_at})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def employee_type_update(request, id):
    if request.method == 'POST':
        employee_type = get_object_or_404(EmployeeType, id=id)
        name = request.POST.get('name')
        employee_type.name = name
        employee_type.save()
        return JsonResponse({'id': employee_type.id, 'name': employee_type.name, 'created_at': employee_type.created_at, 'updated_at': employee_type.updated_at})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def employee_type_delete(request, id):
    if request.method == 'POST':
        employee_type = get_object_or_404(EmployeeType, id=id)
        employee_type.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

# VendorType Views
class VendorTypeListView(ListView):
    model = VendorType
    template_name = 'masters/vendor_type_list.html'
    context_object_name = 'vendor_types'

class VendorTypeCreateView(CreateView):
    model = VendorType
    form_class = VendorTypeForm
    template_name = 'masters/vendor_type_form.html'
    success_url = reverse_lazy('vendor_type_list')

class VendorTypeUpdateView(UpdateView):
    model = VendorType
    form_class = VendorTypeForm
    template_name = 'masters/vendor_type_form.html'
    success_url = reverse_lazy('vendor_type_list')

class VendorTypeDeleteView(DeleteView):
    model = VendorType
    template_name = 'masters/vendor_type_delete.html'
    success_url = reverse_lazy('vendor_type_list')