from rest_framework import serializers
from backend.models import Category
from backend.api.serializers.Service import ServiceSerializer

class CategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description','is_active','created_at', 'services']

