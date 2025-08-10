# backend/views/user.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from accounts.models import UserRole, Role

@login_required
def user_view(request, role):
    if not hasattr(request.user, 'userrole') or request.user.userrole.role.name.lower() != 'admins':
        messages.error(request, "Unauthorized access.")
        return redirect('frontend_home')

    search_query = request.GET.get('search', '')
    users = User.objects.select_related('userrole__role')

    if search_query:
        users = users.filter(username__icontains=search_query) | users.filter(email__icontains=search_query)

    paginator = Paginator(users.order_by('id'), 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    roles = Role.objects.all()

    return render(request, 'backend/users/index.html', {
        'users': page_obj,
        'roles': roles,
        'search_query': search_query,
    })

@login_required
def user_create(request, role):  # ✅ Accept role
    if not hasattr(request.user, 'userrole') or request.user.userrole.role.name.lower() != 'admins':
        messages.error(request, "Unauthorized access.")
        return redirect('frontend_home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        role_id = request.POST.get('role_id')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(
                username=username, email=email,
                first_name=first_name, last_name=last_name,
                password=password
            )
            UserRole.objects.create(user=user, role_id=role_id)
            messages.success(request, "User added successfully.")

    return redirect('admins_user_view', role=role)  # ✅ use passed role

@login_required
def user_update(request, role, user_id):  # ✅ Add role
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        user.save()

        role_id = request.POST.get('role_id')
        UserRole.objects.update_or_create(user=user, defaults={'role_id': role_id})
        messages.success(request, "User updated successfully.")
    return redirect('admins_user_view', role=role)


@login_required
def user_delete(request, role, user_id):  # ✅ Add role
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully.")
    return redirect('admins_user_view', role=role)
