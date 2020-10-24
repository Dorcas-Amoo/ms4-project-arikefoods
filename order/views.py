from django.shortcuts import render

# Create your views here.


def view_order(request):
    """ A view to return the order_cart page """

    return render(request, 'order/order.html')
