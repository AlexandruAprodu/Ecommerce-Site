from django import forms
from shopping_cart.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['shipping_address', 'invoice_address', 'phone_number']
