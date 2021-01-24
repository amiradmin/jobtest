from django import forms

class InsertClinic(forms.Form):
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30 )
    image = forms.ImageField()
