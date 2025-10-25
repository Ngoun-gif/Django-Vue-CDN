from django.urls import path
from . import views


urlpatterns = [

    # Login URLs
    path('sign-In/', views.login_view, name='singin'),

    path('sign-Up/', views.register_view, name='singup'),

    path('sign-Out/', views.logout_view, name='singout'),


]

