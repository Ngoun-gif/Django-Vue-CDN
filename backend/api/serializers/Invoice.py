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


class InvoiceSerializer(serializers.ModelSerializer):
    # Read-only nested serializers
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
        queryset=Service.objects.all(), source='services', many=True, write_only=True
    )
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), source='branch', write_only=True, required=False, allow_null=True
    )
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all(), source='customer', write_only=True
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
        services = validated_data.pop('services', [])
        invoice = Invoice.objects.create(**validated_data)
        invoice.services.set(services)
        invoice.save()  # This will trigger update_totals()
        return invoice

    def update(self, instance, validated_data):
        services = validated_data.pop('services', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if services is not None:
            instance.services.set(services)

        instance.save()  # Trigger total recalculation
        return instance
