# backend/api/urls/Payment.py
from rest_framework.routers import DefaultRouter
from backend.api.views.Payment import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls