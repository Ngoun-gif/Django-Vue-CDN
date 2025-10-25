from django.shortcuts import redirect
from django.contrib.auth import logout
from accounts.models import UserRole, Role

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # ✅ Skip checks for authentication, static, and admin pages
        safe_paths = [
            '/signin/', '/signout/', '/signup/', '/static/', '/admin/', '/admins/'
        ]
        if any(path.startswith(p) for p in safe_paths):
            return self.get_response(request)

        # ✅ Skip for unauthenticated users
        if not request.user.is_authenticated:
            return self.get_response(request)

        # ✅ Auto-assign role for superuser
        if request.user.is_superuser :
            admin_role, _ = Role.objects.get_or_create(name='admins')
            UserRole.objects.get_or_create(user=request.user, role=admin_role)
            return self.get_response(request)

        # ✅ Check for role
        try:
            role = UserRole.objects.get(user=request.user).role.name
        except UserRole.DoesNotExist:
            logout(request)  # Prevent infinite redirect loop
            return redirect('signin')

        # ✅ Role-based restrictions for your custom dashboards
        if path.startswith('/admins/') and role != 'admins':
            return redirect('frontend_home')
        elif path.startswith('/staff/') and role != 'staff':
            return redirect('frontend_home')

        return self.get_response(request)
