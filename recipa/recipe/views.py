from recipe.models import *


def get_recipe(request, **kwargs):
    recipe_url = kwargs.get('recipe').strip()
    rec = Recipe.objects.get(url=recipe_url)
