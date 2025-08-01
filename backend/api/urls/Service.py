from rest_framework.routers import DefaultRouter
from backend.api.views.Service import ServiceViewSet

router = DefaultRouter()
router.register(r'Services', ServiceViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls