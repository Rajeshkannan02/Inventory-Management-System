from django import forms
from .models import Product,Order

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'order_quantity']




class ProductRequestForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()
