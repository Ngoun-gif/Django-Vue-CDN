# backend/api/serializers/Role.py
from rest_framework import serializers
from accounts.models import Role  # adjust to your app name   

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']
