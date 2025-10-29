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
        read_only_fields = ['invoice_number', 'subtotal', 'tax', 'grand_total', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Ensure business rules:
        - Either booking OR (customer + services) must be provided.
        - If booking is provided, customer/branch should not conflict.
        """
        booking = data.get('booking')
        customer = data.get('customer')
        services = data.get('services')

        if booking:
            # If booking is set, customer and branch should match (or be omitted)
            if customer and customer != booking.customer:
                raise serializers.ValidationError(
                    "Customer must match the booking's customer if both are provided."
                )
            if 'branch' in data and data['branch'] != booking.branch:
                raise serializers.ValidationError(
                    "Branch must match the booking's branch if both are provided."
                )
        else:
            # No booking: require customer and at least one service
            if not customer:
                raise serializers.ValidationError("Customer is required when not using a booking.")
            if not services:
                raise serializers.ValidationError("At least one service is required when not using a booking.")

        return data

    def create(self, validated_data):
        services = validated_data.pop('services', [])
        booking = validated_data.get('booking')

        # Create the invoice instance (customer/branch may come from validated_data or booking)
        invoice = Invoice(**validated_data)

        # If booking is provided, auto-fill customer/branch if not already set
        if booking:
            if not invoice.customer:
                invoice.customer = booking.customer
            if not invoice.branch:
                invoice.branch = booking.branch

        # Save first to get PK (needed for M2M and invoice number)
        invoice.save()

        # Set services: from booking or manual list
        if booking:
            invoice.services.set(booking.services.all())
        elif services:
            invoice.services.set(services)

        # The model's save() already recalculates totals, but we already saved.
        # To ensure totals are correct, call update_totals() explicitly or save again.
        # Since our model does it in save(), and we haven't changed services after save,
        # we need to recalculate now:
        invoice.update_totals()
        invoice.save(update_fields=['subtotal', 'tax', 'grand_total'])

        return invoice

    def update(self, instance, validated_data):
        services = validated_data.pop('services', None)

        # Update simple fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update M2M if provided
        if services is not None:
            instance.services.set(services)

        # Recalculate totals
        instance.update_totals()
        instance.save(update_fields=['subtotal', 'tax', 'grand_total', 'updated_at'])

        return instance