
from django.conf.urls import include, url
from django.contrib import admin

from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.forms import SearchForm

from search.views import countries


admin.site.site_header = 'Jobhuntr'
admin.site.site_title = 'Jobhuntr'
admin.site.index_title = '#jobhuntr'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^countries/$', countries, name='countries'),
    url(r'.*', SearchView(
            searchqueryset=SearchQuerySet().order_by('-added_on'),
            form_class=SearchForm
        )
    ),
]
