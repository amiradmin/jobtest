from django import forms

class InsertUser(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30 )
    cell_phone = forms.CharField(max_length=30 )
    birth_date = forms.DateField()
    avatar = forms.ImageField()


class InsertClinicUser(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30 )
    birth_date = forms.DateField()
    avatar = forms.ImageField()
