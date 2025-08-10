# backend/models/booking.py

from django.db import models
from backend.models.customer import Customer
from .branch import Branch
from .product_service import Service

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer} - {self.booking_date}"
