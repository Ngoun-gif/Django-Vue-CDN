# backend/api/urls/__init__.py
from rest_framework.routers import DefaultRouter
from backend.api.views.Branch import BranchViewSet
from backend.api.views.User import UserViewSet
from backend.api.views.Category import CategoryViewSet
from backend.api.views.Booking import BookingViewSet
from backend.api.views.Customer import CustomerViewSet
from backend.api.views.Service import ServiceViewSet
# from backend.api.views.Invoice import InvoiceViewSet
from backend.api.views.Role import RoleViewSet
from backend.api.views.UserRole import UserRoleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'services', ServiceViewSet)
# router.register(r'invoices', InvoiceViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'userroles', UserRoleViewSet)

urlpatterns = router.urls
