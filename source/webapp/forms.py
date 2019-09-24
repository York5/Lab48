from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class GoodForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label="Category")
    stock = forms.IntegerField(required=True, label="Left in Stock", min_value=0)
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True, label='Price')
