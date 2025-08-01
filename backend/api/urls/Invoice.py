from rest_framework.routers import DefaultRouter
from backend.api.views.Invoice import InvoiceSerializer

router = DefaultRouter()
router.register(r'Invoices', InvoiceSerializer)  # 👈 This is what registers /api/users/

urlpatterns = router.urls