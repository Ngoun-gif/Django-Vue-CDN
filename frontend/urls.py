from django.urls import path
from . import views



urlpatterns = [
    # Frontend URLs
    path('', views.frontend_home, name='frontend_home'),  # no leading space in name

    path('home/', views.frontend_home, name='frontend_home'),  # fixed space in name

    path('about/', views.frontend_about, name='frontend_about'),

    path('service/', views.frontend_service, name='frontend_service'),

    path('technician/', views.frontend_technician, name='frontend_technician'),

    path('contact/', views.frontend_contact, name='frontend_contact'),  # lowercase path for consistency

    path('booking/', views.frontend_booking, name='frontend_booking'),


]