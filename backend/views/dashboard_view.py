from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserRole , User
from django.db import IntegrityError
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status , serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


@login_required
def dashboard_view(request, role):
    try:
        user_role = request.user.userrole.role.name.lower()
    except (UserRole.DoesNotExist, AttributeError):
        messages.error(request, "You don't have access.")
        return redirect('frontend_home')

    requested_role = role.lower()

    if user_role != requested_role:
        messages.warning(request, "You don't have permission to view this dashboard.")
        return redirect('frontend_home')

    if user_role not in ['admins', 'staff']:
        return redirect('frontend_home')

    return render(request, 'backend/dashboard/index.html', {
        'user_role': user_role.capitalize()
    })

