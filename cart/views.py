from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from cart.forms import AdressForm
from cart.models import Cart, OrderItem, Order, Adress


@login_required(login_url='/account/login')
def cart(request):
    OrderItemFormSet = modelformset_factory(OrderItem,fields=('quantity',),extra=0)
    cart = Cart.objects.get(user = request.user)
    order,_= Order.objects.get_or_create(cart=cart)
    orderItems = OrderItem.objects.filter(order = order)
    formset = OrderItemFormSet(queryset = orderItems)
    if request.method == "POST":
        formset = OrderItemFormSet(request.POST, queryset= orderItems)
        if(formset.is_valid):
            formset.save()
            orderItems = OrderItem.objects.filter(order=order)
            formset = OrderItemFormSet(queryset=orderItems)
    context = {"cart": cart,
               "ordersForm" : formset}
    return render(request,'pages/cart.html',context)


@login_required(login_url='/account/login')
def shipping(request):
    form = AdressForm()
    adresss = Adress.objects.filter(user=request.user)
    if request.method == 'POST':
        form = AdressForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    context={"form":form,"adresss":adresss}
    return render(request,'pages/shipping.html',context)

@login_required(login_url='/account/login')
def recap(request):
    cart = Cart.objects.get(user=request.user)
    order = Order.objects.get(cart=cart)
    orderItems = OrderItem.objects.filter(order=order)
    return render(request,'pages/recap.html',context={"order":order,"cart":cart,"orderItems":orderItems})

@login_required(login_url='/account/login')
def selectAdress(request,adressId):
    cart = Cart.objects.get(user=request.user)
    order = Order.objects.get(cart=cart)
    order.adress = Adress.objects.get(id=adressId)
    print(order)
    order.save()
    return redirect('cart:shipping')