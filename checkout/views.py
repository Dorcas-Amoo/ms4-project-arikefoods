"""Directly influenced by CI's Boutique Ado Tutorial and codewouter's."""

from django.shortcuts import render, redirect, reverse

from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import OrderLineItem
from menu.models import Menu
from order.contexts import cart_contents

import stripe

"""A view to handle checkout payment. Users are required to login for access"""


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('order', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        order = order_form.save()
        for item_id, item_data in cart.items():
            menu = Menu.objects.get(id=item_id)

            order_line_item = OrderLineItem(
                order_details=order,
                menu=menu,
                quantity=item_data,
            )
            order_line_item.save()

        # Save the info to the user's profile if all is well
        request.session['save_info'] = 'save-info' in request.POST
        return redirect(reverse('checkout_success'))

    else:
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('order', {})
    if not cart:
        return redirect(reverse('menu'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, template, context)


def checkout_success(request):
    """
    Handles successful checkout. Checks that cart's content
    is still present and deletes it,
    then renders the checkout success page.
    """
    if 'order' in request.session:
        del request.session['order']

    return render(request, 'checkout/checkout_success.html')
