from cart.utils import get_or_set_order, check_cart


def get_order(request):
    if request.user.is_authenticated :
        order = get_or_set_order(request)
        check_cart(request)
    else:
        check_cart(request)
        order = request.session.order
    if order is None:
        cart = 0
    else :
        cart = sum([x.quantity for x in order.orderItems.all()])
    return {'order':order,'cart':cart}
