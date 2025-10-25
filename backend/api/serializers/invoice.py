from rest_framework import serializers
from backend.models.invoice import Invoice
from backend.models.invoice_item import InvoiceItem
from backend.models.payment import Payment
from .invoice_item import InvoiceItemSerializer
from .payment import PaymentSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    total_paid = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    balance_due = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_number', 'customer', 'branch', 'booking',
            'issue_date', 'due_date', 'subtotal', 'tax', 'total',
            'status', 'payment_method', 'notes',
            'created_at', 'updated_at',
            'items', 'payments', 'total_paid', 'balance_due',
        ]
        read_only_fields = [
            'invoice_number', 'subtotal', 'tax', 'total',
            'total_paid', 'balance_due', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        """
        Automatically generate invoice_number and calculate totals when creating.
        """
        invoice = Invoice.objects.create(**validated_data)
        invoice.calculate_totals()
        invoice.update_payment_status()
        return invoice

    def update(self, instance, validated_data):
        """
        Update invoice and refresh totals/payment status after save.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.calculate_totals()
        instance.update_payment_status()
        return instance
