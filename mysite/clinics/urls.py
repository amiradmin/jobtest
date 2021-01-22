from django.urls import path,include
from clinics.views import ClinicsView

app_name ="clinics"

urlpatterns = [

    path('clinics/',ClinicsView.as_view(), name='clinics'),




]
