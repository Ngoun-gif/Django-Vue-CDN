# backend/api/views/user.py
from rest_framework import viewsets
from django.contrib.auth.models import User
from backend.api.serializers.User import UserSerializer  # adjust path

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
