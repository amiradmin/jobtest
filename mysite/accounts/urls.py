from rest_framework import routers
from django.contrib import admin
from .views import UserProfile,NewUser,NewClinicUser,Userprofiler,ClinicProfiler
from . import views
from django.urls import include, path
app_name ="accounts"

router = routers.DefaultRouter()
router.register(r'users', views.UserProfile, basename='users')
router.register(r'users/<int:id>', views.UserProfile, basename='users_update')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('newuser/',NewUser.as_view(), name='newuser'),
    path('newclinicuser/',NewClinicUser.as_view(), name='newclinicuser'),
    path('userprofile/',Userprofiler.as_view(), name='userprofile'),
    path('clinicprofile/',ClinicProfiler.as_view(), name='clinicprofile'),
]
