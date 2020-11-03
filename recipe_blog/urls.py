from django.urls import path
from . import views

urlpatterns = [
    path('recipe_blog/', views.recipe_blog, name="recipe_blog"),
]
