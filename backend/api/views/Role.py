# backend/api/views/Role.py
from rest_framework import viewsets
from accounts.models import Role
from backend.api.serializers.Role import RoleSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer