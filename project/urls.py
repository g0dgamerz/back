from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from proj_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_auth.urls')),
]