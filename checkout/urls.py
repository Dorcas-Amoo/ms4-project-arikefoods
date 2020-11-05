from django.urls import path
from . import views
from .webhooks import webhook

""" url paths for checkout, checkout success and webhook pages"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
]
