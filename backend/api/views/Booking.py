from rest_framework import viewsets
from backend.models import Booking
from backend.api.serializers.Booking import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer
