from django import forms
from .models import OrderDetails


class OrderForm(forms.ModelForm):

    """Credits to Codewouter's MS4 project and CI's Boutique Ado."""

    class Meta:
        model = OrderDetails
        fields = (
            'full_name', 'phone_number',
            'street_address1', 'street_address2', 'town_or_city',
            'county', 'postcode', 'country',
        )
