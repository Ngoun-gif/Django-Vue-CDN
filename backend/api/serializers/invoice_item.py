from rest_framework import serializers
from backend.models.invoice_item import InvoiceItem

class InvoiceItemSerializer(serializers.ModelSerializer):
    service_name = serializers.ReadOnlyField(source='service.name')

    class Meta:
        model = InvoiceItem
        fields = ['id', 'service', 'service_name', 'description', 'quantity', 'unit_price', 'total_price']
