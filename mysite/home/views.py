from django.shortcuts import render,get_object_or_404
from clinics.models import Clinics
from django.views.generic import TemplateView

# Create your views here.



class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self):
        print('index')
        context = super(IndexView, self).get_context_data()
        clinic_list =Clinics.objects.all()
        context['clinic_list'] = clinic_list
        return context
