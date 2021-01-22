from rest_framework import routers
from django.contrib import admin
from .views import UserProfile
from . import views
from django.urls import include, path
app_name ="accounts"

router = routers.DefaultRouter()
router.register(r'users', views.UserProfile, basename='users')
router.register(r'users/<int:id>', views.UserProfile, basename='users_update')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
