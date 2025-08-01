from rest_framework import serializers
from backend.models import Booking
from backend.api.serializers.Service import ServiceSerializer
from backend.api.serializers.User import UserSerializer

class BookingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Booking
        fields = '__all__'