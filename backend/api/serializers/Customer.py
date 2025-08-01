from rest_framework import serializers
from backend.models import Customer
from backend.api.serializers.User import UserSerializer

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = '__all__'