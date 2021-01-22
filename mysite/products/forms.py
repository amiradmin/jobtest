from django import forms

class InsertProduct(forms.Form):
    name = forms.CharField(max_length=30)
    product_code = forms.CharField(max_length=30)
    provider = forms.CharField(max_length=30 )
    price = forms.IntegerField()
    image = forms.ImageField()
