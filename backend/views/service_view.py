# backend/view/User.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserRole , User

def service_view(request, role):
    return render(request, 'backend/services/index.html' )
