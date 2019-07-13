from django import forms
from order.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = ('order_list', 'cost', 'content')


