from django.shortcuts import render, redirect,get_object_or_404
from cart.models import Order, Cart
from . import models
from django.views import generic
from .models import Product

def shop(request):
    products = models.Product.objects.all()
    context = {'products' : products}
    return render(request,'pages/shop.html',context)

class ProductView(generic.DetailView):
    template_name = "pages/productDetail.html"
    context_object_name = "product"
    model = Product

def addToCart(request,pk):
    product = get_object_or_404(Product,id=pk)
    cart = Cart.objects.get(user = request.user)
    order,ordered = Order.objects.get_or_create(cart = cart,product=product)
    if not ordered:
        order.quantity+=1
    order.save()
    return redirect('catalogue:productDetail',pk = pk)

def deleteToCart(request,pk,orderId):
    print(orderId)
    get_object_or_404(Order,id=orderId).delete()
    return redirect('cart:cart')
