"""
URL configuration for formsDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urlsd a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formsApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userRegistration/', views.userRegistrationView),
]
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
