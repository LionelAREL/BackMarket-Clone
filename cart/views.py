from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import Cart,Order


@login_required(login_url='/account/login')
def cart(request):
    cart = Cart.objects.get(user = request.user)
    context = {"cart": cart,
               "orders" : Order.objects.filter(cart = cart)}
    return render(request,'pages/cart.html',context)