from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.teacher import Teacher
from backend.api.serializers.teacher import TeacherSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
