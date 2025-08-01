from rest_framework.routers import DefaultRouter
from backend.api.views.Booking import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls