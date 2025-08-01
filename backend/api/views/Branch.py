from rest_framework import viewsets
from backend.models import Branch
from backend.api.serializers.Branch import BranchSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('id')
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'address', 'phone', 'email']  # Fields you want to search
