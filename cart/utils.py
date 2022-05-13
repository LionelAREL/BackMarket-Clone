from cart.models import Order


def get_order(request):
    order,_ = Order.objects.get_or_create(user=request.user,ordered=False)
    return order