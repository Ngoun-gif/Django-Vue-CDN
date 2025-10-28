# backend/api/views/Invoice.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.invoice import Invoice
from backend.api.serializers.Invoice import InvoiceSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer

    # Filtering & search
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    # Search by related customer name, branch name, invoice number
    search_fields = [
        'invoice_number',
        'customer__name',
        'branch__name',
        'status',
        'payment_method',
        'notes',
        'additional_fee'
    ]

    # Exact filtering fields
    filterset_fields = [
        'status',
        'payment_method',
        'branch',
        'customer',
        'booking',
        'invoice_date',
        'additional_fee'

    ]


