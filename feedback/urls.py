from django.urls import path
from . import views

urlpatterns = [
    path('<menu_id>/', views.view_feedback, name='view_feedback'),
    path('add_feedback/<menu_id>/', views.add_feedback, name='add_feedback'),
]
