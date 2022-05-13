from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, RedirectView, DetailView
from cart.utils import get_order
from cart.models import OrderItem
from .models import Product
from django.contrib import messages


class Shop(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'pages/shop.html'

class ProductView(DetailView):
    template_name = "pages/productDetail.html"
    context_object_name = "product"
    model = Product

class AddToCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        order= get_order(self.request)
        product = Product.objects.get(id=kwargs['productId'])
        orderItem,orderedItem = OrderItem.objects.get_or_create(order=order,product=product)
        if not orderedItem:
            if orderItem.quantity > product.stock :
                messages.error(self.request,"Vous essayez de commander plus que ce que l'on possède en stock")
                orderItem.quantity=1
            elif orderItem.quantity == product.stock :
                messages.warning(self.request,'vous ne pouvez commander plus')
                pass
            elif orderItem.quantity == 20:
                messages.warning(self.request,'vous ne pouvez commander plus de 20 articles')
                pass
            else:
                orderItem.quantity +=1
                messages.success(self.request,"vous avez ajouter un article au panier")
        orderItem.save()
        return self.request.GET.get('next')

class Remove(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        order = get_order(self.request)
        orderItem = OrderItem.objects.get(id=kwargs['orderItemId'])
        if orderItem.quantity == 1:
            messages.warning(self.request,"vous avez supprimer l'article du panier")
        else :
            messages.success(self.request,"vous avez supprimer avec succès l'article")
        orderItem.quantity-=1
        orderItem.save()
        return self.request.GET.get('next')

class DeleteToCart(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        get_object_or_404(OrderItem,id=kwargs['orderItemId']).delete()
        messages.success(self.request,"article supprimer avec succès")
        return self.request.GET.get('next')

class BuyOrder(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        orderItem = get_object_or_404(OrderItem,id=kwargs['orderItemId'])
        if orderItem.is_valid():
            orderItem.ordered = True
            product = Product.objects.get(id = orderItem.product.id)
            product.stock -= orderItem.quantity
            product.save()
        orderItem.save()
        return reverse('cart:cart')

class BuyAll(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        order = get_order(self.request)
        can_buy = True
        for orderItem in order.orderItems:
            if not orderItem.is_valid():
                can_buy = False
        if can_buy:
            return reverse('cart:shipping')
        return reverse('cart:cart')
