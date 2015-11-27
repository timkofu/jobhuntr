from django.shortcuts import render
from django.http import HttpResponse


def analytics(request):
    return HttpResponse('1')
