from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'mobile1', 'mobile2', 'email', 'created_at', 'updated_at']
