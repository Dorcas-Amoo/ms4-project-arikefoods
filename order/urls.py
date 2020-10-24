from django.urls import path
from . import views

urlpatterns = [
   path('order_cart/', views.cart, name='order'),
]
