from rest_framework import viewsets
from backend.models import Service
from backend.api.serializers.Service import ServiceSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description','price','duration_minutes','category']  # Fields you want to search
