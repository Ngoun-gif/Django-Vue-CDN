# backend/api/urls/UserRole.py
from rest_framework.routers import DefaultRouter
from backend.api.views.UserRole import UserRoleViewSet  # adjust import path if needed

router = DefaultRouter()
router.register(r'userroles', UserRoleViewSet)  # This registers /api/userroles/

urlpatterns = router.urls
