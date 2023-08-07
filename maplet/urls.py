"""
URL configuration for campus_map project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from core.forms import LoginForm
from profiles.views import profile

urlpatterns = [
    path('', index, name='index'),
    path('locations/', include('location.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile, name='profile'),
    path('directions/', directions, name='directions'),
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'), name='login'),
    path('favorites/', favorites, name='favorites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
