from django.shortcuts import render
from .models import Order

# Create your views here.

def order(request):
    """ A view to return the order page """

    return render(request, 'order/order.html', context)
