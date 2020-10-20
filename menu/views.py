from django.shortcuts import render
from .models import Menu

# Create your views here.


def all_menus(request):

    menus = Menu.objects.all()

    context = {
        'menus': menus,
    }

    return render(request, 'menu/food_menu.html', context)
