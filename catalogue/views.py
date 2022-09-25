from django.shortcuts import redirect,get_object_or_404,render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, RedirectView, DetailView, FormView, View
from django.views.generic.base import ContextMixin

from cart.utils import get_or_set_order
from cart.models import OrderItem
from .forms import SearchForm
from .models import Product, Categorie
from django.contrib import messages
from django.http import JsonResponse

@method_decorator(csrf_exempt, name='dispatch')
class Shop(FormView):
    form_class = SearchForm
    context_object_name = 'products'
    template_name = 'pages/shop.html'

    def get_initial(self):
        initial = super(Shop,self).get_initial()
        initial['search_text'] = self.request.GET.get('search_text')
        if self.request.GET.get('categorie') is not None:
            initial['categorie'] = self.request.GET.get('categorie')
        return initial

    def get_context_data(self, **kwargs):
        context = super(Shop, self).get_context_data(**kwargs)
        products = Product.objects.all()
        search_text = self.request.GET.get('search_text')
        categorie = self.request.GET.get('categorie')
        if search_text and search_text != '':
            products = Product.objects.filter(name__contains=search_text)
        if categorie and categorie != 'tous':
            products = products.filter(categorie__name=categorie)
        context['products'] = products
        return context

def update_cart(request):
    return render(request, 'header.html')

class ProductView(DetailView):
    template_name = "pages/productDetail.html"
    context_object_name = "product"
    model = Product

class AddToCart(View):
    def get(self, *args, **kwargs):
        order= get_or_set_order(self.request)
        product = Product.objects.get(id=kwargs['productId'])
        print(order)
        orderItem,orderedItem = OrderItem.objects.get_or_create(order=order,product=product)
        if not orderedItem:
            if orderItem.quantity > product.stock :
                messages.error(self.request,"Vous essayez de commander plus que ce que l'on possède en stock")
                orderItem.quantity=product.stock
            elif orderItem.quantity == product.stock :
                messages.warning(self.request,'vous ne pouvez commander plus')
            elif orderItem.quantity == 20:
                messages.warning(self.request,'vous ne pouvez commander plus de 20 articles')
            else:
                orderItem.quantity +=1
                messages.success(self.request,"vous avez ajouter un article au panier")
        orderItem.save()
        return JsonResponse({'detail': 'Succeed add to cart item ' + str(kwargs['productId'])})

class Remove(View):
    def get(self, *args, **kwargs):
        order = get_or_set_order(self.request)
        orderItem = OrderItem.objects.get(id=kwargs['orderItemId'])
        if orderItem.quantity == 1:
            messages.warning(self.request,"vous avez supprimer l'article du panier")
        else :
            messages.success(self.request,"vous avez supprimer avec succès l'article")
        orderItem.quantity-=1
        orderItem.save()
        return JsonResponse({'detail': 'Succeed remove order item ' + str(kwargs['orderItemId'])})

class DeleteToCart(View):
    def get(self, *args, **kwargs):
        get_object_or_404(OrderItem,id=kwargs['orderItemId']).delete()
        messages.success(self.request,"article supprimer avec succès")
        return JsonResponse({'detail': 'Succeed remove to cart item ' + kwargs['orderItemId']})

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
        order = get_or_set_order(self.request)
        can_buy = True
        for orderItem in order.orderItems:
            if not orderItem.is_valid():
                can_buy = False
        if can_buy:
            return reverse('cart:shipping')
        return reverse('cart:cart')
