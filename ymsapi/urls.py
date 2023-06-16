"""
URL configuration for ymsapi project.

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
from django.urls import path
from ymsapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ymsapi/stu_list/', views.stu_list),
    path('ymsapi/stu_detail/<int:id>', views.stu_detail),
    path('ymsapi/tea_list/', views.tea_list),
    path('ymsapi/tea_detail/<int:id>', views.tea_detail),
    path('ymsapi/adm_list/', views.adm_list),
    path('ymsapi/adm_detail/<int:id>', views.adm_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)