from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_all_menus, name='menu'),
    path('menu_order/', views.menu_order, name='menu_order'),
]
