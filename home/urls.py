from django.urls import path
from . import views

""" url handlers for the home and contact pages"""

urlpatterns = [
   path('', views.index, name='home'),
   path('contact_us/', views.contact_us, name='contact_us'),
]
