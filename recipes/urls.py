from django.urls import path

from .views import list_recipes, view_recipe

urlpatterns = [
    path('', list_recipes),
    path('<int:id>/', view_recipe),
]
