from django.urls import path
from . import views
from .models import EmployeeType
"""
from .views import (
    EmployeeTypeListView, EmployeeTypeCreateView, EmployeeTypeUpdateView, EmployeeTypeDeleteView,
    VendorTypeListView, VendorTypeCreateView, VendorTypeUpdateView, VendorTypeDeleteView
)
"""
urlpatterns = [
    path('employee-types/', views.employee_type_list, name='employee_type_list'),
    path('employee-types/create/', views.employee_type_create, name='employee_type_create'),
    path('employee-types/update/<int:id>/', views.employee_type_update, name='employee_type_update'),
    path('employee-types/delete/<int:id>/', views.employee_type_delete, name='employee_type_delete'),
]

