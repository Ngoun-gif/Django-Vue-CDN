from rest_framework import viewsets
from backend.models import Invoice
from backend.api.serializers.Invoice import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer