from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from recipe import views as recipe_views
from category.api import CategoryResource
from recipe.api import RecipeResource


v1_api = Api(api_name='v1')
v1_api.register(CategoryResource())
v1_api.register(RecipeResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe/(?P<recipe>[-\w]+)/$', recipe_views.get_recipe, name='get_recipe'),
    url(r'^api/', include(v1_api.urls)),
)
