from django.urls import path
from backend.views.dashboard_view import dashboard_view
from backend.views.branch_view import branch_view

urlpatterns = [
    path('<str:role>/dashboard/', dashboard_view, name='role_dashboard'),

     path('<str:role>/branch/', branch_view, name='role_branch'),
]
