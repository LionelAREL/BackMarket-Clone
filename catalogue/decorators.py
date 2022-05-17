from functools import wraps
from django.http import HttpResponseRedirect
from cart.utils import get_or_set_order
from django.contrib import messages


def order_required(view_func,redirect_url='/cart/'):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if get_or_set_order(request).orderItems.count() != 0:
                return view_func(request, *args, **kwargs)
            else:
                messages.add_message(request,messages.WARNING,"veuillez mettre des articles dans le panier")
                return HttpResponseRedirect(redirect_url)
        else:
            messages.add_message(request, messages.WARNING, "veuillez vous connecter pour effectuer vos achats")
            return HttpResponseRedirect(redirect_url)
    return _wrapped_view


def adress_required(view_func,redirect_url='/cart/shipping/'):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            if get_or_set_order(request).adress is not None:
                return view_func(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.WARNING, "veuillez choisir une adresse de livraison")
                return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponseRedirect(redirect_url)
    return _wrapped_view