from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.subject import Subject
from backend.api.serializers.Subject import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
