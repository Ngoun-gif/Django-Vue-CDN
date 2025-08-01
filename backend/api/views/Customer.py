from rest_framework import viewsets
from backend.models import Customer
from backend.api.serializers.Customer import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer