from django.urls import path,include
from clinics.views import ClinicsView,NewClinic,ClinicDetails

app_name ="clinics"

urlpatterns = [

    path('clinics/',ClinicsView.as_view(), name='clinics'),
    path('newclinics/',NewClinic.as_view(), name='newclinics'),
    path('details/<int:id>/',ClinicDetails.as_view(), name='clinic_details'),



]
