from rest_framework import serializers
from recipe.models import Recipe
from submitter.serializers import SubmitterSerializer
from category.serializers import CategorySerializer


class RecipeSerializer(serializers.ModelSerializer):
    submitter = SubmitterSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('recipeid',
                  'title',
                  'intro',
                  'ingredients',
                  'instructions',
                  'endcomments',
                  'url',
                  'submitter',
                  'category')
