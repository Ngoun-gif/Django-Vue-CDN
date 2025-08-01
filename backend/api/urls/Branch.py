from rest_framework.routers import DefaultRouter
from backend.api.views.Branch import BranchViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet)  # 👈 This is what registers /api/users/

urlpatterns = router.urls