# masters/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from .models import EmployeeType, VendorType
from .forms import EmployeeTypeForm, VendorTypeForm
from django import forms
from django.http import JsonResponse

def welcome(request):
    return render(request, 'welcome.html')

# EmployeeType Views
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