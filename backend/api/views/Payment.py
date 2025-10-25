from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from backend.models.payment import Payment
from backend.api.serializers.payment import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('-payment_date')
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['invoice', 'payment_method']
