
import json

from django.shortcuts import render
from django.http import JsonResponse


def search(request):

    if request.method == 'GET':
        return render(request, 'search.html')
    elif request.method == 'POST':
        pass
