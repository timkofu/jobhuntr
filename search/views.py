from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.cache import cache_page

from .models import Country


@cache_page(3600)
def countries(request: HttpRequest) -> HttpResponse:

    # Show contries in which job posts are being indexed
    return render(
        request, "countries.html", {"countries": Country.objects.only("name", "a2code")}
    )
