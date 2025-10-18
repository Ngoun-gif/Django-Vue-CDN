from django.db import models
from django.utils import timezone
from .booking import Booking
from .customer import Customer
from .branch import Branch

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    booking = models.OneToOneField(
        Booking,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='invoice'
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)

    invoice_number = models.CharField(max_length=50, unique=True)
    issue_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(null=True, blank=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='unpaid'
    )

    payment_method = models.CharField(
        max_length=30,
        choices=[
            ('cash', 'Cash'),
            ('credit_card', 'Credit Card'),
            ('bank_transfer', 'Bank Transfer'),
            ('online', 'Online'),
        ],
        blank=True,
        null=True
    )

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.customer.name}"

    def calculate_totals(self):
        """Recalculate subtotal, tax, and total from items"""
        items = self.items.all()
        self.subtotal = sum(item.total_price for item in items)
        self.tax = self.subtotal * 0.1  # Example: 10% VAT
        self.total = self.subtotal + self.tax
        self.save()

    @property
    def total_paid(self):
        """Sum of all payments linked to this invoice"""
        return sum(payment.amount for payment in self.payments.all())

    @property
    def balance_due(self):
        """Remaining amount to be paid"""
        return self.total - self.total_paid

    def update_payment_status(self):
        """Automatically update invoice status based on payments"""
        paid = self.total_paid
        if paid >= self.total:
            self.status = 'paid'
        elif paid > 0:
            self.status = 'partial'
        else:
            self.status = 'unpaid'
        self.save()
