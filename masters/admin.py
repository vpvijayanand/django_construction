# masters/admin.py
from django.contrib import admin
from .models import EmployeeType, VendorType

admin.site.register(EmployeeType)
admin.site.register(VendorType)
