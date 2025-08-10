# backend/api/serializers/Serivce.py
from rest_framework import serializers
from backend.models import Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price', 'duration_minutes', 'category']