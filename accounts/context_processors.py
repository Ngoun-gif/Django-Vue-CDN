# accounts/context_processors.py
from .models import UserRole

def user_role(request):
    if request.user.is_authenticated:
        try:
            role = UserRole.objects.get(user=request.user).role.name.lower()
            return {'user_role': role}
        except UserRole.DoesNotExist:
            return {'user_role': None}
    return {'user_role': None}
