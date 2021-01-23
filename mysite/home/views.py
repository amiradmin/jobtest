from django.shortcuts import render,get_object_or_404
from clinics.models import Clinics
from django.views.generic import TemplateView
from django.db.models import Q
from home.forms import SearchForm
# Create your views here.



class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self):
        print('index')
        context = super(IndexView, self).get_context_data()
        clinic_list =Clinics.objects.all()
        form = SearchForm()
        context['clinic_list'] = clinic_list
        context['form'] = form
        return context


    def post(self, request, *args, **kwargs):
        print('Search Post')
        form = SearchForm(self.request.POST)
        field = request.POST['field']
        search_list = Clinics.objects.filter(
            Q(name__icontains=field) | Q(field__icontains=field)
        )
        return render(request,'search_results.html',{'search_list':search_list})

class SearchResultsView(TemplateView):
    model = Clinics
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Clinics.objects.filter(
            Q(name__icontains=query) | Q(field__icontains=query)
        )
        return object_list
