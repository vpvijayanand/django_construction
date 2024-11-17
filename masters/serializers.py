# masters/serializers.py
from rest_framework import serializers
from .models import EmployeeType, VendorType

class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['id', 'name', 'created_at', 'updated_at']

class VendorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorType
        fields = ['id', 'name', 'created_at', 'updated_at']
