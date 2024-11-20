# masters/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from .models import BrandType, EmployeeType, VendorType,EmployeeRolles
from .forms import EmployeeType, VendorType,BrandType,EmployeeRolles,Iteam
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


# Vendor Type Views
def vendor_type_list(request):
    vendor_types = VendorType.objects.all()
    return render(request, 'masters/vendor_Type_list.html', {'Vendor_Types': vendor_types})

def vendor_type_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        vendor_type = VendorType.objects.create(name=name)
        return JsonResponse({'id': vendor_type.id, 'name': vendor_type.name, 'created_at': vendor_type.created_at, 'updated_at': vendor_type.updated_at})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def vendor_type_update(request, id):
    if request.method == 'POST':
        vendor_type = get_object_or_404(VendorType, id=id)
        name = request.POST.get('name')
        vendor_type.name = name
        vendor_type.save()
        return JsonResponse({'id': vendor_type.id, 'name': vendor_type.name, 'created_at': vendor_type.created_at, 'updated_at': vendor_type.updated_at})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def vendor_type_delete(request, id):
    if request.method == 'POST':
        vendor_type = get_object_or_404(VendorType, id=id)
        vendor_type.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

# Brand Type Views

def brand_type_list(request):
    brand_types = BrandType.objects.all()
    return render(request, 'masters/brand_type_list.html', {'brand_types': brand_types})

def brand_type_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand_type = BrandType.objects.create(name=name)
        return JsonResponse({
            'id': brand_type.id,
            'name': brand_type.name,
            'created_at': brand_type.created_at,
            'updated_at': brand_type.updated_at
        })
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def brand_type_update(request, id):
    if request.method == 'POST':
        brand_type = get_object_or_404(BrandType, id=id)
        name = request.POST.get('name')
        brand_type.name = name
        brand_type.save()
        return JsonResponse({
            'id': brand_type.id,
            'name': brand_type.name,
            'created_at': brand_type.created_at,
            'updated_at': brand_type.updated_at
        })
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def brand_type_delete(request, id):
    if request.method == 'POST':
        brand_type = get_object_or_404(BrandType, id=id)
        brand_type.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

# employee_rolles Views

def employee_rolles_list(request):
    employee_rolles = EmployeeRolles.objects.all()
    return render(request, 'masters/employee_rolles_list.html', {'employee_rolles': employee_rolles})

def employee_rolles_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employee_rolle = EmployeeRolles.objects.create(name=name)
        return JsonResponse({
            'id': employee_rolle.id,
            'name': employee_rolle.name,
            'created_at': employee_rolle.created_at,
            'updated_at': employee_rolle.updated_at
        })
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def employee_rolles_update(request, id):
    if request.method == 'POST':
        employee_rolle = get_object_or_404(EmployeeRolles, id=id)
        name = request.POST.get('name')
        employee_rolle.name = name
        employee_rolle.save()
        return JsonResponse({
            'id': employee_rolle.id,
            'name': employee_rolle.name,
            'created_at': employee_rolle.created_at,
            'updated_at': employee_rolle.updated_at
        })
    return JsonResponse({'error': 'Invalid Request'}, status=400)

def employee_rolles_delete(request, id):
    if request.method == 'POST':
        employee_rolle = get_object_or_404(EmployeeRolles, id=id)
        employee_rolle.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid Request'}, status=400)

# Iteam Views

# List all iteams
def iteam_list(request):
    iteams = Iteam.objects.select_related('brand').all()
    brand_types = BrandType.objects.all()  # Fetch all brands
    return render(request, 'masters/iteam_list.html', {'iteams': iteams, 'brand_types': brand_types})

# Create a new iteam

def iteam_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand_id = request.POST.get('brand_id')
        brand = get_object_or_404(BrandType, id=brand_id)
        iteam = Iteam.objects.create(name=name, brand=brand)
        return JsonResponse({
            'id': iteam.id,
            'name': iteam.name,
            'brand': iteam.brand.name,
            'created_at': iteam.created_at,
            'updated_at': iteam.updated_at
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Update an existing iteam
def iteam_update(request, id):
    if request.method == 'POST':
        iteam = get_object_or_404(Iteam, id=id)
        name = request.POST.get('name')
        brand_id = request.POST.get('brand_id')
        brand = get_object_or_404(BrandType, id=brand_id)
        iteam.name = name
        iteam.brand = brand
        iteam.save()
        return JsonResponse({
            'id': iteam.id,
            'name': iteam.name,
            'brand': iteam.brand.name,
            'created_at': iteam.created_at,
            'updated_at': iteam.updated_at
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Delete an iteam
def iteam_delete(request, id):
    if request.method == 'POST':
        iteam = get_object_or_404(Iteam, id=id)
        iteam.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)