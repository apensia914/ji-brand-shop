from django.shortcuts import render
from . import models 

def home(request):
    return render(request, "users/home.html")

def about(request):
    return render(request, "users/about.html")