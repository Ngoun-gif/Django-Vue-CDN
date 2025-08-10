"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

urlpatterns = [
     path('admin/', admin.site.urls),  # Django admin panel
    path('', include('accounts.urls')),  # for login/register/logout
    path('', include('frontend.urls')),  # public pages (home, service, etc.)
    path('', include('backend.urls')),
    path('api/', include('backend.api.urls')),

   path("csrf/", ensure_csrf_cookie(TemplateView.as_view(template_name="blank.html")), name="csrf"),
]
