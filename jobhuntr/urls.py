from django.conf.urls import include, url
from django.contrib import admin

from haystack.query import SearchQuerySet
from haystack.views import SearchView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # #url(r'.*', 'search.views.search', name='search'),
    url(r'^countries/$', 'search.views.countries', name='countries'),
    url(r'.*', SearchView(
            searchqueryset=SearchQuerySet().order_by('-added_on')
        )),
]
