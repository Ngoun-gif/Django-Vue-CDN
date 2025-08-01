from django import template
from accounts.models import UserRole  # Change if your model is elsewhere

register = template.Library()

@register.filter(name='has_role')
def has_role(user, role_name):
    if user.is_authenticated:
        try:
            return user.userrole.role.name.lower() == role_name.lower()
        except (UserRole.DoesNotExist, AttributeError):
            return False
    return False