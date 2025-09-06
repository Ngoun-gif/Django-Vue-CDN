from rest_framework.routers import DefaultRouter
from backend.api.views.teacher import TeacherViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls