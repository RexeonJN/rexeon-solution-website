"""rexeonsolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rexeonapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('blog/', views.blog.as_view(), name = 'blog'),
    path('group/', views.group),
    path('services/', views.service),
    path('career/', views.career),
    path('contact/', views.contact),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.blog_detail.as_view(), name='blog_detail'),
    path('apply/', views.apply_form), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
