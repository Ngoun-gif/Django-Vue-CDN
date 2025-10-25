# backend/api/urls/InvoiceItem.py
from rest_framework.routers import DefaultRouter
from backend.api.views.InvoiceItem import InvoiceItem

router = DefaultRouter()
router.register(r'invoiceitems', InvoiceItem)  # 👈 This is what registers /api/users/

urlpatterns = router.urls