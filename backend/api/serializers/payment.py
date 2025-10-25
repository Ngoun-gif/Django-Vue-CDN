from rest_framework import serializers
from backend.models.payment import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'amount', 'payment_date', 'payment_method', 'reference_no', 'note', 'created_at']
