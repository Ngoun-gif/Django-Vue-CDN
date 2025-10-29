# backend/api/serializers/Invoice.py
from rest_framework import serializers
from backend.models.service import Service
from backend.models.invoice import Invoice
from backend.models.branch import Branch
from backend.models.customer import Customer
from backend.models.booking import Booking
from backend.api.serializers.Service import ServiceSerializer
from backend.api.serializers.Customer import CustomerSerializer
from backend.api.serializers.Branch import BranchSerializer
from backend.api.serializers.Booking import BookingSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    # Read-only nested serializers
    booking = BookingSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    services = ServiceSerializer(read_only=True, many=True)
    payment_method_display = serializers.CharField(source='get_payment_method_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    # Write-only fields
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking', write_only=True, required=False, allow_null=True
    )
    service_ids = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(), source='services', many=True, write_only=True, required=False
    )
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), source='branch', write_only=True, required=False, allow_null=True
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Invoice
        fields = [
            'id',
            'invoice_number',
            'invoice_date',
            'branch',
            'branch_id',
            'customer',
            'customer_id',
            'booking',
            'booking_id',
            'services',
            'service_ids',
            'subtotal',
            'tax',
            'additional_fee',
            'grand_total',
            'status',
            'status_display',
            'payment_method',
            'payment_method_display',
            'notes',
            'payment_deadline',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['subtotal', 'tax', 'grand_total', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Allow creating invoice either:
        - From manual service_ids, OR
        - From an existing booking (auto-copy details)
        """
        services = validated_data.pop('services', [])
        booking = validated_data.get('booking', None)

        # Create invoice instance
        invoice = Invoice(**validated_data)

        # If created from a booking
        if booking:
            # Auto-copy related info
            invoice.customer = booking.customer
            invoice.branch = booking.branch
            invoice.save()  # Need to save before setting M2M
            invoice.services.set(booking.services.all())
        else:
            invoice.save()
            if services:
                invoice.services.set(services)

        # Trigger total recalculation
        invoice.save()
        return invoice

    def update(self, instance, validated_data):
        services = validated_data.pop('services', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if services is not None:
            instance.services.set(services)

        instance.save()  # Trigger recalculation
        return instance
