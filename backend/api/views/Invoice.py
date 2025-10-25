from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.invoice import Invoice
from backend.api.serializers.invoice import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-issue_date')
    serializer_class = InvoiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter by fields
    filterset_fields = ['customer', 'branch', 'status', 'payment_method']
    search_fields = ['invoice_number', 'customer__name', 'branch__name']
    ordering_fields = ['issue_date', 'total', 'subtotal', 'status']
