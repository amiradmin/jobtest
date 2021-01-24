from django.shortcuts import render,get_object_or_404
from clinics.models import Clinics
from django.views.generic import TemplateView
from clinics.forms import InsertClinic
from booking.models import Queues
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.




class ClinicDetails(LoginRequiredMixin,TemplateView):

    template_name='clinics/clinic_details.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_clinics = self.get_object()
        patent_in_queue =Queues.objects.filter(user = self.request.user).count()
        context['patent_in_queue'] = patent_in_queue
        context['single_clinics'] = single_clinics

        return context

    def get_object(self):
         return get_object_or_404(Clinics, pk=self.kwargs.get("id"))


class ClinicsView(TemplateView):
    template_name = "index.html"


    def get_context_data(self):
        print('ClinicsView')
        context = super(ClinicsView, self).get_context_data()
        clinic_list =Clinics.objects.all()
        context['clinic_list'] = clinic_list
        return context



class NewClinic(TemplateView):
    template_name = "clinics/new_clinics.html"

    def get_context_data(self):

        context = super(NewClinic, self).get_context_data()
        form = InsertClinic()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        print('Post')
        form = InsertClinic(self.request.POST,self.request.FILES)
        clinic_list =Clinics.objects.all()
        clinic_obj = Clinics()
        print( request.user)
        clinic_obj.user = request.user
        clinic_obj.name = request.POST.get("name")
        clinic_obj.address = request.POST.get("address")
        clinic_obj.phone = request.POST.get("phone")
        clinic_obj.image = request.FILES['image']
        clinic_obj.save()
        return render(request,'index.html',{'clinic_list':clinic_list})
