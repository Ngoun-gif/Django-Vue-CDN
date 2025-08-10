# backend/api/serializers/customer.py
from rest_framework import serializers
from backend.models.customer import Customer
from django.contrib.auth.models import User
from accounts.models import Role, UserRole

class CustomerSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='user.username', read_only=True)
    role_name = serializers.CharField(source='user.userrole.role.name', read_only=True)

    # Optional fields for creation
    username = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    role_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Customer
        fields = [
            'id', 'customer_name', 'role_name', 'phone', 'address',
            'date_of_birth', 'gender', 'created_at',
            'username', 'email', 'password', 'role_id'
        ]
        read_only_fields = ['id', 'created_at', 'customer_name', 'role_name']

    def create(self, validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email', f"{username}@example.com")
        password = validated_data.pop('password', '123456')
        role_id = validated_data.pop('role_id')

        # Create User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Assign Role
        role = Role.objects.get(id=role_id)
        UserRole.objects.create(user=user, role=role)

        # Create Customer
        customer = Customer.objects.create(
            user=user,
            **validated_data
        )
        return customer

    def update(self, instance, validated_data):
        # Handle username update with uniqueness check
        username = validated_data.pop('username', None)
        if username and instance.user.username != username:
            if User.objects.filter(username=username).exclude(id=instance.user.id).exists():
                raise serializers.ValidationError({'username': 'This username is already taken.'})
            instance.user.username = username
            instance.user.save()

        # Update editable Customer fields
        for field in ['phone', 'address', 'gender', 'date_of_birth']:
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        instance.save()
        return instance
