# backend/api/views/invoice.py
# from rest_framework import viewsets
# from backend.models.invoice import Invoice
# from backend.api.serializers.Invoice import InvoiceSerializer
#
# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer
#
#     def get_queryset(self):
#         booking_id = self.request.query_params.get('booking_id')
#         if booking_id:
#             return Invoice.objects.filter(booking_id=booking_id)
#         return Invoice.objects.all()
