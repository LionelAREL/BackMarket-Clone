from django.shortcuts import render
from . import models
from django.views import generic


def shop(request):
    products = models.Product.objects.all()
    context = {'products' : products}
    return render(request,'pages/shop.html',context)