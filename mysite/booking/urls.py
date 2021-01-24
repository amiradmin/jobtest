from django.urls import path,include
from booking.views import NewBooking

app_name ="booking"

urlpatterns = [

    path('newbooking/<int:id>/',NewBooking.as_view(), name='newbooking_'),




]
