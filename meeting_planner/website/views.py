from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def date(request):
    return HttpResponse("This oage served at" + str(datetime.now()))

# Create your views here.
