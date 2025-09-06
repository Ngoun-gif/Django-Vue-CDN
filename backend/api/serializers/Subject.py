from rest_framework import serializers
from backend.models.subject import Subject
from backend.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True, source='teacher_set')

    class Meta:
        model = Subject
        fields = '__all__'
