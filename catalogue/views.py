from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from cart.models import Order, Cart, OrderItem
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

def addToCart(request,productId):
    cart = Cart.objects.get(user = request.user)
    order,ordered = Order.objects.get_or_create(cart = cart,ordered=False)
    product = Product.objects.get(id=productId)
    orderItem,orderedItem = OrderItem.objects.get_or_create(order=order,product=product)
    if not orderedItem:
        orderItem.quantity+=1
    orderItem.save()
    print(request.GET.get('next'))
    return HttpResponseRedirect(request.GET.get('next'))

def remove(request,orderItemId):
    orderItem,orderedItem = OrderItem.objects.get_or_create(id = orderItemId)
    if not orderedItem:
        orderItem.quantity-=1
    orderItem.save()
    print(request.GET.get('next'))
    return HttpResponseRedirect(request.GET.get('next'))

def deleteToCart(request,orderItemId):
    get_object_or_404(OrderItem,id=orderItemId).delete()
    return redirect('cart:cart')

def buyOrder(request,orderItemId):
    orderItem = get_object_or_404(OrderItem,id=orderItemId)
    if orderItem.is_valid():
        orderItem.ordered = True
        product = Product.objects.get(id = orderItem.product.id)
        product.stock -= orderItem.quantity
        product.save()
    orderItem.save()
    return redirect('cart:cart')

def buyAll(request):
    cart = get_object_or_404(Cart,user = request.user)
    orders = Order.objects.filter(cart=cart)
    can_buy = True
    for orderItem in orders.orderItem_set:
        if not orderItem.is_valid():
            can_buy = False
    if can_buy:
        for orderItem in orders.orderItem_set:
            return redirect('cart:shipping')
    return redirect('cart:cart')
