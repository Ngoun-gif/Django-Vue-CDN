from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserRole , User


def teacher_view(request,role):
    return render(request, 'backend/teacher/index.html' )
