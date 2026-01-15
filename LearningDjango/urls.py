"""
URL configuration for LearningDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from LearningDjango import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.aboutUs),
    path('home/', views.Home),
    path('dynamic/<int:courseId>', views.DynamicRoute),
    path('dynamic/<str:courseName>', views.DynamicRoute),
    path('dynamic/<slug:coursename>', views.DynamicRoute),
    path('dynamicadata/<PassAnyValue>', views.DynamicRouteAnyData),
    
]
