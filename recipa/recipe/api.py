from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
from category.api import CategoryResource
from recipe.models import Recipe


class RecipeResource(ModelResource):
    category = fields.ManyToManyField(CategoryResource, 'category')

    class Meta:
        queryset = Recipe.objects.all()
        resource_name = 'recipe'
        authorization = DjangoAuthorization()