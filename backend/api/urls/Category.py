from rest_framework.routers import DefaultRouter
from backend.api.views.Category import CategoryViewSet

router = DefaultRouter()
router.register(r'Categories', CategoryViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls