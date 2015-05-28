from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from tastypie import fields
from category.models import Category
from recipe.api import RecipeResource


class CategoryResource(ModelResource):
    recipes = fields.ManyToManyField(RecipeResource, attribute='recipe_set', null=True)

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        # these should be replaced when sent to prod; only for testing
        authentication = Authentication()
        authorization = Authorization()
