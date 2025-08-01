from rest_framework.routers import DefaultRouter
from backend.api.views.Customer import CustomerViewSet

router = DefaultRouter()
router.register(r'bookings', CustomerViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls