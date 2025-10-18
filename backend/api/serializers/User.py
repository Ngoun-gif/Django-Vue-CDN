# accounts/api/serializers/user_serializer.py
from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import UserRole, Role
from backend.models.customer import Customer

class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='userrole.role.name', read_only=True)
    role_id = serializers.IntegerField(write_only=True, required=True)
    password = serializers.CharField(write_only=True)
    active = serializers.BooleanField(source='is_active')  # alias field

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'active',         # API name
            'role_name',
            'role_id'
        ]

    def create(self, validated_data):
        role_id = validated_data.pop('role_id')
        password = validated_data.pop('password')

        # Extract and map active -> is_active
        active_status = validated_data.pop('is_active', True)

        # Create user
        user = User(**validated_data)
        user.is_active = active_status
        user.set_password(password)
        user.save()

        # Assign role
        role = Role.objects.get(id=role_id)
        UserRole.objects.create(user=user, role=role)

        #


    def update(self, instance, validated_data):
        role_id = validated_data.pop('role_id', None)
        password = validated_data.pop('password', None)
        active_status = validated_data.pop('is_active', instance.is_active)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.is_active = active_status

        if password:
            instance.set_password(password)

        instance.save()

        # Update role
        if role_id:
            role = Role.objects.get(id=role_id)
            if hasattr(instance, 'userrole'):
                instance.userrole.role = role
                instance.userrole.save()
            else:
                UserRole.objects.create(user=instance, role=role)



        return instance
