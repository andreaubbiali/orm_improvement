from django.shortcuts import render
from django.http import HttpResponse


def getProduct(request):
    return HttpResponse("Product is bb.")