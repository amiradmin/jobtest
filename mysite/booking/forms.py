from django import forms

class InsertNewBooking(forms.Form):
    date = forms.CharField(max_length=30)
