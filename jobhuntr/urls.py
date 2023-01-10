from django.urls import re_path
from django.contrib import admin

from haystack.query import SearchQuerySet
from haystack.views import SearchView
from haystack.forms import SearchForm

from search.views import countries


admin.site.site_header = "Jobhuntr"
admin.site.site_title = "Jobhuntr"
admin.site.index_title = "#jobhuntr"


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^countries/$", countries, name="countries"),
    re_path(
        r".*",
        SearchView(
            searchqueryset=SearchQuerySet().order_by("-added_on"), form_class=SearchForm
        ),
    ),
]
