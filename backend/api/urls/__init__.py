from rest_framework.routers import DefaultRouter
from backend.api.views.Branch import BranchViewSet
from backend.api.views.User import UserViewSet
from backend.api.views.Category import CategoryViewSet

from backend.api.views.Booking import BookingViewSet
from backend.api.views.Customer import CustomerViewSet
from backend.api.views.Service import ServiceViewSet
from backend.api.views.Invoice import InvoiceViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)  # 👈 This is what registers  
router.register(r'categories', CategoryViewSet)  # 👈 This is what registers /api/categories/
router.register(r'branches', BranchViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = router.urls