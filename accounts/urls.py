from django.urls import path
from . import views


urlpatterns = [

    # Login URLs
    path('sign-In/', views.login_view, name='login'),

    path('sign-Up/', views.register_view, name='register'),

    path('sign-Out/', views.logout_view, name='logout'),


]

