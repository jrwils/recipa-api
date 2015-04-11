from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipe.models import *
from recipe.serializers import RecipeSerializer


@api_view()
def get_recipe(request, **kwargs):
    recipe_url = kwargs.get('recipe').strip()
    rec = Recipe.objects.get(url=recipe_url)
    serializer = RecipeSerializer(rec, many=False)
    return Response(serializer.data)