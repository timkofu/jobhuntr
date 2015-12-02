from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # #url(r'.*', 'search.views.search', name='search'),
    url(r'.*', include('haystack.urls')),
]
