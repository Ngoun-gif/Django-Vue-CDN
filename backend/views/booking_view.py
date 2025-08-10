from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import UserRole , User




def booking_view(request, role):
    return render(request, 'backend/booking/index.html' )
