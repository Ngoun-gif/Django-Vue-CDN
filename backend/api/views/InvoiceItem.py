from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.invoice_item import InvoiceItem
from backend.api.serializers.invoice_item import InvoiceItemSerializer

class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['invoice', 'service']
