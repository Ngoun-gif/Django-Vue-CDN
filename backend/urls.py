from django.urls import path
from backend.views.dashboard_view import dashboard_view
from backend.views.branch_view import branch_view
from backend.views.category_view import category_view
from backend.views.booking_view import booking_view
from backend.views.service_view import service_view
from backend.views.user_view import user_view, user_create, user_update, user_delete
from backend.views.customer_view import customer_view
from backend.views.subject_view import subject_view
from backend.views.teacher_view import teacher_view





urlpatterns = [
    
    path('<str:role>/dashboard/', dashboard_view, name='role_dashboard'),

    path('<str:role>/branch/', branch_view, name='role_branch'),

    path('<str:role>/category/', category_view, name='role_category'),

    path('<str:role>/booking/', booking_view, name='role_booking'),

    path('<str:role>/service/', service_view, name='role_service'),

    path('<str:role>/user/', user_view, name='role_user'),

    path('<str:role>/customer/', customer_view, name='role_customer'),
    path('<str:role>/subject/', subject_view, name='role_subject'),
    path('<str:role>/teacher/', teacher_view, name='role_teacher'),






    path('<str:role>/user/', user_view, name='admins_user_view'),
    path('<str:role>/user/add/', user_create, name='admins_user_add'),
    path('<str:role>/user/update/<int:user_id>/', user_update, name='admins_user_update'),
    path('<str:role>/user/delete/<int:user_id>/', user_delete, name='admins_user_delete'),



    

]
