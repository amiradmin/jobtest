from django import forms

class SearchForm(forms.Form):
    field = forms.CharField(max_length=30)
