from rest_framework import serializers
from backend.models import Invoice
from backend.api.serializers.Booking import BookingSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    
    class Meta:
        model = Invoice
        fields = '__all__'