# backend/api/urls/Role.py
from rest_framework.routers import DefaultRouter
from backend.api.views.Role import RoleViewSet

router = DefaultRouter()
router.register(r'Roles', RoleViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls