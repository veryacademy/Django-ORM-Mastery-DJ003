from django import forms

class Payment(forms.Form):
  payor = forms.CharField(max_length=30)
  payee = forms.CharField(max_length=30)
  amount = forms.CharField(max_length=30)

