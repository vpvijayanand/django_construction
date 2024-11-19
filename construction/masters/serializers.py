# masters/serializers.py
from rest_framework import serializers
from .models import EmployeeType, VendorType ,BrandType,EmployeeRolles

class EmployeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['id', 'name', 'created_at', 'updated_at']

class VendorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorType
        fields = ['id', 'name', 'created_at', 'updated_at']

class BrandTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandType
        fields = ['id', 'name', 'created_at', 'updated_at']

class EmployeeRolleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRolles
        fields = ['id', 'name', 'created_at', 'updated_at']


class IteamSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')  # Display associated brand name

    class Meta:
        model = Iteam
        fields = ['id', 'name', 'brand_name', 'brand', 'created_at', 'updated_at']
        # 'brand' is the ForeignKey ID, 'brand_name' is the related name for display