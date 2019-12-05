"""BudgetManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('main/', TemplateView.as_view(template_name='main.html'), name='main'),
    #path('main2/', TemplateView.as_view(template_name='main2.html'), name='main2'),
    #path('main3/', TemplateView.as_view(template_name='main3.html'), name='main3'),
    path('main4/', TemplateView.as_view(template_name='main4.html'), name='main4'),
    path('',include('Manager.urls'))
]
