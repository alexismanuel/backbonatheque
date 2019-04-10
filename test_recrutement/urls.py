"""test_recrutement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from creatorz.api import MusicianViewSet, WriterViewSet, CustomerViewSet, PlayErrorViewSet
from major.urls import major_router
from creatorz.views import albums, play

api_router = DefaultRouter()
api_router.register(r'musician', MusicianViewSet)
api_router.register(r'writer', WriterViewSet)
api_router.register(r'customers', CustomerViewSet)
api_router.register(r'play_errors', PlayErrorViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls + major_router.urls)),
    path('django-rq/', include('django_rq.urls')),
    path('albums', albums),
    path('<int:customer_id>/<int:album_id>/play/', play)
]
