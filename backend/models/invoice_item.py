from django.db import models
from .invoice import Invoice
from .service import Service

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='items'
    )
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        """Auto-calculate total price"""
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service.name if self.service else 'Item'} x {self.quantity}"
