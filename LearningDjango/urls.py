"""
URL configuration for LearningDjango project.

The `urlpatterns` list routes URLs to O1_views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function O1_views
    1. Add an import:  from my_app import O1_views
    2. Add a URL to urlpatterns:  path('', O1_views.home, name='home')
Class-based O1_views
    1. Add an import:  from other_app.O1_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from LearningDjango import O1_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', O1_views.aboutUs),
    path('home/', O1_views.Home, name=""),
    path('dynamic/<int:courseId>', O1_views.DynamicRoute),
    path('dynamic/<str:courseName>', O1_views.DynamicRoute),
    path('dynamic/<slug:coursename>', O1_views.DynamicRoute),
    path('dynamicadata/<PassAnyValue>', O1_views.DynamicRouteAnyData),
    path('', O1_views.HomePage, name="home"),
    path('pass/', O1_views.PassData),
    path('dataInLoop/', O1_views.PassDataLoop),
    path('css_style/',O1_views.Webpage),
    path('fullweb/',O1_views.Website),
    path('contact/', O1_views.Contact, name="contact"),
    path('thank-you/', O1_views.ThankYou, name="thank_you"),
    path('service/', O1_views.Service, name="service"),
    path('about-us/', O1_views.About, name="aboutus"),
    path('login/', O1_views.Form, name="form"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
