# backend/api/views/Customer.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models import Customer
from backend.api.serializers.Customer import  CustomerSerializer , CustomerCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class CustomerViewSet(viewsets.ModelViewSet):
    # The default queryset should remain broad, but we'll modify it in get_queryset
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated]  # Add your permission classes here
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'phone']

    def get_serializer_class(self):
        if self.action in ['create']:
            return CustomerCreateSerializer
        return CustomerSerializer

    permission_classes = [AllowAny]