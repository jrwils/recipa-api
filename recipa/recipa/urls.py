from django.conf.urls import patterns, include, url
from django.contrib import admin
from recipe import views as recipe_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^recipe/(?P<recipe>[-\w]+)/$', recipe_views.get_recipe, name='get_recipe'),
)
