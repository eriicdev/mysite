from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Página inicial do blog")

# Create your views here.
