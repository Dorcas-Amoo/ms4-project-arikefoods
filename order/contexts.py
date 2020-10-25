from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Menu


def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('order', {})

    for item_id, quantity in cart.items():
        menu = get_object_or_404(Menu, pk=item_id)
        total += quantity * menu.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'menu': menu,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context
