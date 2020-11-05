from django.shortcuts import render
from .models import RecipePost


# Create your views here.


def recipe_blog(request):
    """ A view to return the recipe blog page """

    posts = RecipePost.objects.all()

    template = 'recipe_blog/recipe.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
