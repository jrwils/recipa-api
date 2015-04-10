from rest_framework import serializers
from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    # set up a Nested Relationship to display both submitter name and ID
    # http://www.django-rest-framework.org/api-guide/relations/
    submitter = serializers.StringRelatedField()

    class Meta:
        model = Recipe
