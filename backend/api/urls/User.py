# backend/api/urls/User.py
from rest_framework.routers import DefaultRouter
from backend.api.views.User import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls