# backend/api/views/Booking.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from backend.models import Booking
from backend.api.serializers.Booking import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('id')
    serializer_class = BookingSerializer

    # Enable filtering backends
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    # Fields allowed for search (full-text)
    search_fields = [
        'customer__user__username',  # Search by customer's username
        'branch__name',              # If branch has a name field
        'service__name',             # Service name
        'status',
        'notes',
    ]

    # Fields allowed for exact filtering
    filterset_fields = ['status', 'booking_date', 'branch', 'customer', 'service']