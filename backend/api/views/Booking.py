# backend/api/views/Booking.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models import Booking
from backend.api.serializers.Booking import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    search_fields = [
        'customer__user__username',
        'branch__name',
        'services__name',  # ✅ plural
        'status',
        'notes',
    ]

    filterset_fields = [
        'status',
        'booking_date',
        'branch',
        'customer',
        'services',  # ✅ plural
    ]
