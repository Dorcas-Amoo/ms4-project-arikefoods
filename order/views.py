from django.shortcuts import render, redirect
from django.contrib import messages

from menu.models import Menu

# Create your views here.

""" Credits to CI's Boutique Ado Tutorial """


def view_order(request):
    """ A view to return the order_cart page """

    return render(request, 'order/order.html')


def add_to_cart(request, item_id):
    """ A view to add items quantity to the order_cart """

    menu = Menu.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('order', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {menu.name} to your cart')

    request.session['order'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """
    Adjusts quantity of each menu in the cart.
    (Influenced by Code Institute Boutique Ado tutorial)
    """
    redirect_url = request.POST.get('redirect_url')

    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('order', {})
        if quantity >= 0 and quantity <= 100:
            if quantity > 0:
                cart[item_id] = quantity
            else:
                cart.pop(item_id)

            request.session['order'] = cart
            return redirect(redirect_url)
        else:
            return redirect(redirect_url)
    else:
        return redirect(redirect_url)
