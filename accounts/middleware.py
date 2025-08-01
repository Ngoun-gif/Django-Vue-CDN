from django.shortcuts import redirect
from django.contrib.auth import logout
from accounts.models import UserRole

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # ✅ Skip checks for authentication and static/auth pages
        safe_paths = [
            '/login/', '/logout/', '/register/', '/admins/', '/static/'
        ]
        if any(path.startswith(p) for p in safe_paths):
            return self.get_response(request)

        # ✅ Skip for unauthenticated users
        if not request.user.is_authenticated:
            return self.get_response(request)

        # ✅ Check for role
        try:
            role = UserRole.objects.get(user=request.user).role.name
        except UserRole.DoesNotExist:
            logout(request)  # Prevent infinite redirect loop
            return redirect('login')

        # ✅ Role-based restrictions
        if path.startswith('/admins/') and role != 'Admin':
            return redirect('frontend_home')
        elif path.startswith('/staff/') and role != 'Staff':
            return redirect('frontend_home')

        return self.get_response(request)
