from rest_framework import viewsets
from backend.models import Service
from backend.api.serializers.Service import ServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer