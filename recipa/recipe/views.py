from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipe.models import *
from recipe.serializers import RecipeSerializer


@api_view()
def get_recipe(request, recipe_id):
    rec = Recipe.objects.get(recipeid=recipe_id)
    serializer = RecipeSerializer(rec, many=False)
    return Response(serializer.data)