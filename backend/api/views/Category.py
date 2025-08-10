from rest_framework import viewsets
from backend.models import Category
from backend.api.serializers.Category import CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description']  # Fields you want to search
