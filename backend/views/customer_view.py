# backend/views/customer.py

from django.shortcuts import render, redirect


def customer_view(request,role):
    return render(request, 'backend/customers/index.html' )
