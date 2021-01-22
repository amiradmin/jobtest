from django.shortcuts import render,get_object_or_404
from products.models import Product
from django.views.generic import TemplateView

# Create your views here.



class IndexView(TemplateView):
    template_name = "index.html"


    def get_context_data(self):
        print('index')
        context = super(IndexView, self).get_context_data()
        product_list =Product.objects.all()
        context['product_list'] = product_list
        return context
