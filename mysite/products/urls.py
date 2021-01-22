from django.urls import path,include
from products.views import ProductView,NewProduct,DeleteProduct

app_name ="products"

urlpatterns = [
    # path('postcontent/<int:id>/',views.post_detail, name='post_content'),
    # path('updatepost/<int:id>/',views.UpdatePost.as_view(), name='update_post_'),
    # path('updateslider/<int:id>/',views.UpdateSlider.as_view(), name='update_slider_'),
    # # path('trainingcontent/<int:id>/',views.training_post_detail, name='training_post_content'),

    path('allproduct/',ProductView.as_view(), name='all_product'),
    path('newproduct/',NewProduct.as_view(), name='new__product'),
    path('delproduct/<int:id>',DeleteProduct.as_view(), name='delproduct'),



]
