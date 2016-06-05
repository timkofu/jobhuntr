from django.conf.urls import include, url
from django.contrib import admin

from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView

from search.views import countries


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # #url(r'.*', 'search.views.search', name='search'),
    url(r'^countries/$', countries, name='countries'),
    url(r'.*', SearchView(
            searchqueryset=SearchQuerySet().filter(boolean_field=1)\
            .order_by('-added_on')
        ).as_view()),
]
