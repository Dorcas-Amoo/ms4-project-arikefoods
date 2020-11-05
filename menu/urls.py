from django.urls import path
from . import views

""" url handlers for the food menu and order pages"""


urlpatterns = [
    path('', views.view_all_menus, name='menu'),
    path('menu_order/', views.menu_order, name='menu_order'),
]
