# masters/admin.py
from django.contrib import admin
from .models import EmployeeType, VendorType,BrandType,EmployeeRolles

admin.site.register(EmployeeType)
admin.site.register(VendorType)
admin.site.register(BrandType)
admin.site.register(EmployeeRolles)
