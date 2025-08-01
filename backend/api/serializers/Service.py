from rest_framework import serializers
from backend.models import Service
from backend.api.serializers.Category import CategorySerializer

class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Service
        fields = '__all__'