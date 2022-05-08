from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render
from cart.models import Cart, OrderItem, Order


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