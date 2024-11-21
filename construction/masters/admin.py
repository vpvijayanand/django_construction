# masters/admin.py
from django.contrib import admin
from .models import EmployeeType,BrandType,EmployeeRolles,Item,vendortype

admin.site.register(EmployeeType)
admin.site.register(vendortype)
admin.site.register(BrandType)
admin.site.register(EmployeeRolles)
admin.site.register(Item)