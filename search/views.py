
# #import json

from django.shortcuts import render
# #from django.http import HttpResponse
# #from django.core import serializers
from django.views.decorators.cache import cache_page

from .models import Country


@cache_page(3600)
def countries(request):

    #return HttpResponse(
    #    serializers.serialize("xml", Country.objects.only('name', 'a2code')),
    #    content_type="application/xml"
    #)

    # Show contries in which job posts are being indexed
    return render(
        request,
        'countries.html',
        {'countries': Country.objects.only('name', 'a2code')}
    )
