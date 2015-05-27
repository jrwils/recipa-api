from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipe import views as recipe_views
from category.api import CategoryResource

category_resource = CategoryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe/(?P<recipe>[-\w]+)/$', recipe_views.get_recipe, name='get_recipe'),
    url(r'^api/', include(category_resource.urls)),
)
