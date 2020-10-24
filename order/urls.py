from django.urls import path
from . import views

urlpatterns = [
   path('order_cart/', views.view_order, name='view_order'),
]
