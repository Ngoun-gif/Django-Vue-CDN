# backend/api/views/customer.py
from rest_framework import viewsets, permissions, filters
from backend.models.customer import Customer
from backend.api.serializers.Customer import CustomerSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.select_related('user', 'user__userrole', 'user__userrole__role').all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['user__username', 'phone', 'address', 'gender']
    filterset_fields = ['gender']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
