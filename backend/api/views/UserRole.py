# backend/api/views/UserRole.py

from rest_framework import viewsets
from accounts.models import UserRole
from backend.api.serializers.UserRole import UserRoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
