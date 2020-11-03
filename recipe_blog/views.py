from django.shortcuts import render

# Create your views here.


def recipe_blog(request):
    """ A view to return the recipe blog page """

    return render(request, 'recipe_blog/recipe.html')
