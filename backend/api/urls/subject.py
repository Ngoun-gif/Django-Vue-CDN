from rest_framework.routers import DefaultRouter
from backend.api.views.subject import SubjectViewSet

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls