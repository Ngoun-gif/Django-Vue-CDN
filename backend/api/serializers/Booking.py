# backend/api/serializers/Booking.py
from rest_framework import serializers
from backend.models.booking import Booking
from backend.api.serializers.Customer import CustomerSerializer
from backend.api.serializers.Branch import BranchSerializer
from backend.api.serializers.Service import ServiceSerializer
from backend.models.customer import Customer
from backend.models.branch import Branch
from backend.models.service import Service

# backend/api/serializers/Booking.py
class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    services = ServiceSerializer(read_only=True, many=True)

    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer', write_only=True)
    branch_id = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), source='branch', write_only=True)
    service_ids = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), source='services', many=True, write_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'customer', 'customer_id',
            'branch', 'branch_id',
            'services', 'service_ids',
            'booking_date',
            'booking_time',
            'status',
            'notes',
        ]

