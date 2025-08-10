# backend/api/serializers/Booking.py
from rest_framework import serializers
from backend.models.booking import Booking
from backend.models.customer import Customer
from backend.models.branch import Branch
from backend.models.product_service import Service
from backend.api.serializers.Customer import CustomerSerializer
from backend.api.serializers.Branch import BranchSerializer
from backend.api.serializers.Service import ServiceSerializer

class BookingSerializer(serializers.ModelSerializer):
    # Nested read-only serializers
    customer = CustomerSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    service = ServiceSerializer(read_only=True)

    # Write-only fields to accept IDs on create/update
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(),
        source='customer',
        write_only=True
    )
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(),
        source='branch',
        write_only=True
    )
    service_id = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        source='service',
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id',
            'customer', 'customer_id',
            'branch', 'branch_id',
            'service', 'service_id',
            'booking_date',
            'booking_time',
            'status',
            'notes',
        ]

