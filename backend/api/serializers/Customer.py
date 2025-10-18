from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Role, UserRole
from backend.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    role_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            'id', 'username', 'role_name',
            'name', 'address', 'date_of_birth', 'gender', 'phone', 'created_at'
        ]
        read_only_fields = ['id', 'username', 'role_name', 'created_at']

    def get_role_name(self, obj):
        user_role = UserRole.objects.filter(user=obj.user).first()
        return user_role.role.name if user_role else None


class CustomerCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    role_name = serializers.CharField(write_only=True, default='Customer')

    class Meta:
        model = Customer
        fields = [
            'id', 'username', 'password', 'role_name',
            'name', 'address', 'date_of_birth', 'gender', 'phone', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        role_name = validated_data.pop('role_name')

        # Create User
        user = User.objects.create_user(username=username, password=password)

        # Get or Create Role
        role, _ = Role.objects.get_or_create(name=role_name)

        # Assign Role
        UserRole.objects.create(user=user, role=role)

        # Create Customer
        customer = Customer.objects.create(user=user, **validated_data)
        return customer
