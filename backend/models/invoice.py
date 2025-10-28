# backend/models/invoice.py
from django.db import models
from django.utils import timezone
from backend.models.customer import Customer
from backend.models.branch import Branch
from backend.models.booking import Booking
from backend.models.service import Service


class Invoice(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('issued', 'Issued'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('other', 'Other'),
    ]

    invoice_number = models.CharField(max_length=20, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    services = models.ManyToManyField(Service, blank=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    additional_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    notes = models.TextField(blank=True, null=True)
    invoice_date = models.DateField(default=timezone.now)
    payment_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_invoice_number(self):
        """Auto-generate invoice number like INV-20251028-001"""
        date_part = timezone.now().strftime("%Y%m%d")
        count_today = Invoice.objects.filter(invoice_date__date=timezone.now().date()).count() + 1
        return f"INV-{date_part}-{count_today:03d}"

    def update_totals(self):
        """Calculate subtotal, tax, and grand total"""
        if self.booking:
            subtotal = sum(float(s.price) for s in self.booking.services.all())
        else:
            subtotal = sum(float(s.price) for s in self.services.all())

        self.subtotal = subtotal
        self.tax = subtotal * 0.10  # 10% tax
        self.grand_total = subtotal + self.tax + float(self.additional_fee or 0)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()

        super().save(*args, **kwargs)  # Save first to ensure we have an ID
        self.update_totals()
        super().save(update_fields=['subtotal', 'tax', 'grand_total'])

    def __str__(self):
        return f"{self.invoice_number} - {self.customer.name if self.customer else 'No Customer'}"
