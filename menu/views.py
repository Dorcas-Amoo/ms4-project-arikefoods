from django.shortcuts import render
from .models import Menu

# Create your views here.

""" Credits to CI's Boutique Ado Tutorial """


def view_all_menus(request):
    """ A view to return the food menu page """

    menus = Menu.objects.all()

    context = {
        'menus': menus,
    }

    return render(request, 'menu/food_menu.html', context)


def menu_order(request):
    """ A view to return the menu order page """

    menus = Menu.objects.all()

    context = {
        'menus': menus,
    }

    return render(request, 'menu/menu_order.html', context)
