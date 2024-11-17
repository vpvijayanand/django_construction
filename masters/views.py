# masters/views.py
"""
from rest_framework import generics
from django.shortcuts import render
from .models import EmployeeType, VendorType
from .serializers import EmployeeTypeSerializer, VendorTypeSerializer

# EmployeeType Views
class EmployeeTypeListCreate(generics.ListCreateAPIView):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer

class EmployeeTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer

# VendorType Views
class VendorTypeListCreate(generics.ListCreateAPIView):
    queryset = VendorType.objects.all()
    serializer_class = VendorTypeSerializer

class VendorTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorType.objects.all()
    serializer_class = VendorTypeSerializer


def employee_type_list(request):
    employee_types = EmployeeType.objects.all()
    return render(request, 'masters/employee_type_list.html', {'employee_types': employee_types})

# View for VendorType
def vendor_type_list(request):
    vendor_types = VendorType.objects.all()
    return render(request, 'masters/vendor_type_list.html', {'vendor_types': vendor_types})
"""
# masters/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeType, VendorType
from .forms import EmployeeTypeForm, VendorTypeForm

# EmployeeType CRUD Views
def employee_type_list(request):
    employee_types = EmployeeType.objects.all()
    return render(request, 'masters/employee_type_list.html', {'employee_types': employee_types})

def employee_type_create(request):
    if request.method == 'POST':
        form = EmployeeTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_type_list')
    else:
        form = EmployeeTypeForm()
    return render(request, 'masters/employee_type_form.html', {'form': form})

def employee_type_edit(request, id):
    employee_type = get_object_or_404(EmployeeType, id=id)
    if request.method == 'POST':
        form = EmployeeTypeForm(request.POST, instance=employee_type)
        if form.is_valid():
            form.save()
            return redirect('employee_type_list')
    else:
        form = EmployeeTypeForm(instance=employee_type)
    return render(request, 'masters/employee_type_form.html', {'form': form})

def employee_type_delete(request, id):
    employee_type = get_object_or_404(EmployeeType, id=id)
    employee_type.delete()
    return redirect('employee_type_list')

# VendorType CRUD Views
def vendor_type_list(request):
    vendor_types = VendorType.objects.all()
    return render(request, 'masters/vendor_type_list.html', {'vendor_types': vendor_types})

def vendor_type_create(request):
    if request.method == 'POST':
        form = VendorTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_type_list')
    else:
        form = VendorTypeForm()
    return render(request, 'masters/vendor_type_form.html', {'form': form})

def vendor_type_edit(request, id):
    vendor_type = get_object_or_404(VendorType, id=id)
    if request.method == 'POST':
        form = VendorTypeForm(request.POST, instance=vendor_type)
        if form.is_valid():
            form.save()
            return redirect('vendor_type_list')
    else:
        form = VendorTypeForm(instance=vendor_type)
    return render(request, 'masters/vendor_type_form.html', {'form': form})

def vendor_type_delete(request, id):
    vendor_type = get_object_or_404(VendorType, id=id)
    vendor_type.delete()
    return redirect('vendor_type_list')
