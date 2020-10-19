from django.shortcuts import render
from .models import Menu

# Create your views here.

def menu(request):
    menu = Menu.objects.all()
    context = {
        'menus': menu
    }
    return render(request, 'menu/food_menu.html', context)

