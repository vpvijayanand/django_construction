# masters/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # EmployeeType URLs
    #path('employee-types/', views.EmployeeTypeListCreate.as_view(), name='employee-type-list-create'),
    #path('employee-types/<int:pk>/', views.EmployeeTypeRetrieveUpdateDestroy.as_view(), name='employee-type-retrieve-update-destroy'),

    # VendorType URLs
    #path('vendor-types/', views.VendorTypeListCreate.as_view(), name='vendor-type-list-create'),
    #path('vendor-types/<int:pk>/', views.VendorTypeRetrieveUpdateDestroy.as_view(), name='vendor-type-retrieve-update-destroy'),
    #path('employee-types/', views.employee_type_list, name='employee_type_list'),
    #path('vendor-types/', views.vendor_type_list, name='vendor_type_list'),

    path('employee-types/', views.employee_type_list, name='employee_type_list'),
    path('employee-types/create/', views.employee_type_create, name='employee_type_create'),
    path('employee-types/<int:id>/edit/', views.employee_type_edit, name='employee_type_edit'),
    path('employee-types/<int:id>/delete/', views.employee_type_delete, name='employee_type_delete'),
    
    # Vendor Type URLs
    path('vendor-types/', views.vendor_type_list, name='vendor_type_list'),
    path('vendor-types/create/', views.vendor_type_create, name='vendor_type_create'),
    path('vendor-types/<int:id>/edit/', views.vendor_type_edit, name='vendor_type_edit'),
    path('vendor-types/<int:id>/delete/', views.vendor_type_delete, name='vendor_type_delete'),
]
