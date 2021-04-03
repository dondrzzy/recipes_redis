from django.shortcuts import render

from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings

from .models import Category, Recipe
# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def list_recipes(request):

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes.html', context)


def view_recipe(request, id):
    if cache.get(id):
        recipe = cache.get(id)
        print("DATA from CACHE")
    else:
        try:
            recipe = Recipe.objects.get(id=id)
            cache.set(id, recipe)
            print("DATA from DB")
        except Recipe.DoesNotExist:
            return redirect('/')
    context = {'recipe': recipe}
    return render(request, 'view_recipe.html', context)
