from django.shortcuts import render
from catalogue import models

def home(request):
    return render(request,'pages/home.html')
