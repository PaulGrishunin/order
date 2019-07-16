from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_item', 'cost', 'comment')
        labels = { 'order_item':'zakaz', 'cost':'stoimost', 'comment':'komentariy' }


class OrderString(forms.Form):
    slug = forms.SlugField()
    order_item = forms.CharField(max_length=200)
    cost = forms.IntegerField()
    comment = forms.CharField()
    action = forms.CharField()