from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from category.models import Category


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = DjangoAuthorization()
