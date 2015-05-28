from tastypie.authorization import DjangoAuthorization
from auth.recipa_authentication import RecipaAuthentication
from tastypie.resources import ModelResource
from tastypie import fields
from recipe.models import Recipe


class RecipeResource(ModelResource):
    class Meta:
        queryset = Recipe.objects.all()
        resource_name = 'recipe'
        authentication = RecipaAuthentication()
