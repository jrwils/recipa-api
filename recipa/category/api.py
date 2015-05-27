from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie import fields
from category.models import Category
from recipe.api import RecipeResource


class CategoryResource(ModelResource):
    recipes = fields.ManyToManyField(RecipeResource, attribute='recipe_set', null=True)

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = DjangoAuthorization()
