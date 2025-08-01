from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserRole, Role
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ---------------------
# Login View
# ---------------------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            try:
                user_role = user.userrole.role.name.lower()
            except Exception:
                logout(request)  # ✅ logout to stop session loop
                messages.error(request, "Role not assigned.")
                return redirect('login')

            if user_role in ['admins', 'staff']:
                return redirect('role_dashboard', role=user_role)
            else:
                return redirect('frontend_home')
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'auth/login.html')




# ---------------------
# Register View
# ---------------------
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if not username or not password or not email:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'auth/register.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)

            # Assign default role (Customer)
            customer_role, _ = Role.objects.get_or_create(name='Customer')
            UserRole.objects.create(user=user, role=customer_role)

            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')

        except IntegrityError:
            messages.error(request, 'Username already exists. Please choose another.')
        except Exception as e:
            messages.error(request, f'Unexpected error: {str(e)}')

    return render(request, 'auth/register.html')


# ---------------------
# Logout View
# ---------------------
def logout_view(request):
    logout(request)
    return redirect('frontend_home')


