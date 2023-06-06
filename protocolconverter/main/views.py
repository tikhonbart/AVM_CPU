from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("страница")


def categories(request):
    return HttpResponse("<h1>fasdfasdf</h1>")