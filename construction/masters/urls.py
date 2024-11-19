from django.urls import path
from . import views

# from .models import EmployeeType,VendorType,BrandType,EmployeeRolles,Iteam

# from .views import (
#     employeeTypeListView, employeeTypeCreateView, employeeTypeUpdateView, employeeTypeDeleteView,
#     VendorTypeListView, VendorTypeCreateView, VendorTypeUpdateView, VendorTypeDeleteView
# )

urlpatterns = [
    path('employee-types/', views.employee_type_list, name='employee_type_list'),
    path('employee-types/create/', views.employee_type_create, name='employee_type_create'),
    path('employee-types/update/<int:id>/', views.employee_type_update, name='employee_type_update'),
    path('employee-types/delete/<int:id>/', views.employee_type_delete, name='employee_type_delete'),
    
    path('Vendor-Type/', views.vendor_type_list, name='vendor_type_list'),
    path('Vendor-Type/create/', views.vendor_type_create, name='vendor_type_create'),
    path('Vendor-Type/update/<int:id>/', views.vendor_type_update, name='vendor_type_update'),
    path('Vendor-Type/delete/<int:id>/', views.vendor_type_delete, name='vendor_type_delete'),

    path('brand-type/', views.brand_type_list, name='brand_type_list'),
    path('brand-type/create/', views.brand_type_create, name='brand_type_create'),
    path('brand-type/update/<int:id>/', views.brand_type_update, name='brand_type_update'),
    path('brand-type/delete/<int:id>/', views.brand_type_delete, name='brand_type_delete'),

    path('employee-rolles/', views.employee_rolles_list, name='employee_rolles_list'),
    path('employee-rolles/create/', views.employee_rolles_create, name='employee_rolles_create'),
    path('employee-rolles/update/<int:id>/', views.employee_rolles_update, name='employee_rolles_update'),
    path('employee-rolles/delete/<int:id>/', views.employee_rolles_delete, name='employee_rolles_delete'),
    
    path('iteams/', views.iteam_list, name='iteam_list'),  # List all iteams
    path('iteams/create/', views.iteam_create, name='iteam_create'),  # Create a new iteam
    path('iteams/update/<int:id>/', views.iteam_update, name='iteam_update'),  # Update an iteam
    path('iteams/delete/<int:id>/', views.iteam_delete, name='iteam_delete'),  # Delete an iteam
]

