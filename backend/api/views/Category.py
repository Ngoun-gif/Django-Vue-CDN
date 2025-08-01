from rest_framework import viewsets
from backend.models import Category
from backend.api.serializers.Category import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer