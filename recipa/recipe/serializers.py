from rest_framework import serializers
from recipe.models import Recipe
from submitter.serializers import SubmitterSerializer


class RecipeSerializer(serializers.ModelSerializer):
    submitter = SubmitterSerializer()

    class Meta:
        model = Recipe
        fields = ('recipeid',
                  'title',
                  'intro',
                  'ingredients',
                  'instructions',
                  'endcomments',
                  'url',
                  'submitter')
