# backend/models/invoice.py
from decimal import Decimal
from django.core.exceptions import ValidationError
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

    invoice_number = models.CharField(max_length=20, unique=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    services = models.ManyToManyField(Service, blank=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    additional_fee = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    notes = models.TextField(blank=True, null=True)
    invoice_date = models.DateField(default=timezone.now)
    payment_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['invoice_date']),
            models.Index(fields=['status']),
            models.Index(fields=['customer']),
            models.Index(fields=['booking']),
        ]
        ordering = ['-invoice_date', '-created_at']

    def clean(self):
        """Ensure business rules are met."""
        if not self.customer and not self.booking:
            raise ValidationError("Invoice must be associated with either a customer or a booking.")
        if self.booking and self.customer and self.booking.customer != self.customer:
            raise ValidationError("Booking's customer must match the invoice customer if both are set.")

    def generate_invoice_number(self):
        """Generate a unique, safe invoice number like INV-20251029-000123 using the object's PK."""
        if not self.pk:
            raise RuntimeError("Invoice must be saved before generating an invoice number.")
        date_part = self.invoice_date.strftime("%Y%m%d")
        return f"INV-{date_part}-{self.pk:06d}"

    def update_totals(self):
        """Recalculate subtotal, tax (10%), and grand total."""
        # Determine source of services
        if self.booking:
            service_prices = [s.price for s in self.booking.services.all()]
        else:
            service_prices = [s.price for s in self.services.all()]

        self.subtotal = sum(service_prices, Decimal('0.00'))
        self.tax = (self.subtotal * Decimal('0.10')).quantize(Decimal('0.01'))  # 10% tax
        self.grand_total = self.subtotal + self.tax + self.additional_fee

    def save(self, *args, **kwargs):
        # Ensure invoice_date is set for new invoices
        if self.pk is None and not self.invoice_date:
            self.invoice_date = timezone.now().date()

        # First save to get a primary key
        super().save(*args, **kwargs)

        # Generate invoice number if missing (only for new instances)
        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()
            super().save(update_fields=['invoice_number'])

        # Always update financial totals
        self.update_totals()
        super().save(update_fields=['subtotal', 'tax', 'grand_total'])

    def __str__(self):
        customer_name = self.customer.name if self.customer else "No Customer"
        return f"{self.invoice_number} - {customer_name}"