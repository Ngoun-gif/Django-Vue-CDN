# backend/api/views/User.py

from rest_framework import viewsets
from django.contrib.auth.models import User
from backend.api.serializers.User import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.select_related('userrole__role').all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']

