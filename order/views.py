from django.shortcuts import render, redirect

# Create your views here.


def view_order(request):
    """ A view to return the order_cart page """

    return render(request, 'order/order.html')


def add_to_cart(request, item_id):
    """ A view to add items quantity to the order_cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('order', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['order'] = cart
    print(request.session['order'])
    return redirect(redirect_url)
