from django.urls import path
from . import views
from .models import EmployeeType

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
]

