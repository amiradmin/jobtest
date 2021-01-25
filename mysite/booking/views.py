from django.shortcuts import render
from booking.models import Queues
from clinics.models import Clinics
from booking.forms import InsertNewBooking
from django.views.generic import TemplateView
import datetime
# Create your views here.


class NewBooking(TemplateView):
    template_name = "booking/new_booking.html"

    def get_context_data(self , **kwargs):

        context = super(NewBooking, self).get_context_data()
        form = InsertNewBooking()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        print('Booking Post')
        form = InsertNewBooking(self.request.POST)
        print( request.user)
        booked_date= request.POST.get("date")
        booking_obj = Queues()
        booking_obj.user = request.user
        booking_obj.clinic = Clinics.objects.get(pk = self.kwargs.get("id"))
        last_booking = Queues.objects.select_related('clinic').filter(clinic=booking_obj.clinic).last()
        booking_obj.date = last_booking.date + datetime.timedelta(0,1800)
        print(booking_obj.date)
        booking_obj.save()
        return render(request,'index.html',{})
