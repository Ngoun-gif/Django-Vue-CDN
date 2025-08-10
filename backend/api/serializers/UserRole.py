# backend/api/serializers/UserRole.py
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import UserRole, Role
from backend.api.serializers.Role import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # To show user details
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    role = RoleSerializer(read_only=True)  # To show role details
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source='role', write_only=True
    )

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'user_id', 'role', 'role_id']
