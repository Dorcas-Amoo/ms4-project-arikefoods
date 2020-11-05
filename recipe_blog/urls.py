from django.urls import path
from . import views

""" Url handler for the blog page """


urlpatterns = [
    path('recipe_blog/', views.recipe_blog, name="recipe_blog"),
]
