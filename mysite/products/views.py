from django.shortcuts import render,get_object_or_404
from products.models import Product
from django.views.generic import TemplateView
from .forms import InsertProduct
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
# Create your views here.



class ProductView(TemplateView):
    template_name = "products/list.html"
    permission_classes = (IsAuthenticated,)

    def get_context_data(self):
        print('Test')
        context = super(ProductView, self).get_context_data()
        product_list =Product.objects.all()
        context['product_list'] = product_list
        return context

    # def post(self, request, *args, **kwargs):
    #
    #     form = OrderForm(self.request.POST)
    #     if form.is_valid():
    #         print("Submited")


class NewProduct(TemplateView):
    template_name = "products/new_product.html"

    def get_context_data(self):

        context = super(NewProduct, self).get_context_data()
        form = InsertProduct()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        print('Post')
        form = InsertProduct(self.request.POST,self.request.FILES)
        product_list = Product.objects.all()
        product_obj = Product()
        print( request.user)
        product_obj.user = request.user
        product_obj.name = request.POST.get("name")
        product_obj.product_code = request.POST.get("product_code")
        product_obj.provider = request.POST.get("provider")
        product_obj.price = int(request.POST.get("price"))
        product_obj.image = request.FILES['image']
        product_obj.save()
        return render(request,'products/list.html',{'product_list':product_list})


class DeleteProduct(TemplateView):
    template_name = "products/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_product = self.get_object()
        single_product.delete()

        print('Deleted')
        return None

    def get_object(self):
         return get_object_or_404(Product, pk=self.kwargs.get("id"))
