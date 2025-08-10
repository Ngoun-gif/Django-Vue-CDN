# backend/api/urls/Customer.py
from rest_framework.routers import DefaultRouter
from backend.api.views.Customer import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls