from django.shortcuts import render
from .models import Order

# Create your views here.


def cart(request):
    """ A view to return the order_cart page """

    return render(request, 'order/order.html')
