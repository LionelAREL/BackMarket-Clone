from cart.models import Order
from catalogue.models import Product


def get_or_set_order(request):
    if request.user.is_authenticated :
        merge_cart(request)
        order,_ = Order.objects.get_or_create(user=request.user,ordered=False)

    else :
        if request.session.order is None:
            order = Order(ordered = False)
            order.save()
            request.session.order = order
        else :
            order = request.session.order
    return order


def refresh_quantity(order):
    for orderItem in order.orderItems.all():
        pdt = orderItem.product
        pdt.stock = pdt.stock - orderItem.quantity
        pdt.save()
    order.ordered = True
    order.save()

def get_order(request):
    if request.user.is_authenticated :
        order = get_or_set_order(request)
    else:
        order = request.session.order
    return order

def merge_cart(request):
    # on fusionne les 2 carts
    if request.session.order is not None :
        order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
        for orderItem in request.session.order.orderItems.all():
            print("orderItem.product ", orderItem.product.id)
            print("Product.objects.filter(orderItems__in=order.orderItems.all()) ",
                  [x.id for x in Product.objects.filter(orderItems__in=order.orderItems.all())])
            if orderItem.product in Product.objects.filter(orderItems__in=order.orderItems.all()):
                print("yess")
                ord = order.orderItems.get(product=orderItem.product)
                ord.quantity = ord.quantity + orderItem.quantity
                ord.save()
                orderItem.delete()
        request.session.order.orderItems.update(order=order)
        request.session.order.delete()
        request.session.order = None

        if not order.is_valid():
            for orderItem in order.orderItems.all():
                if not orderItem.is_valid():
                    orderItem.quantity = orderItem.product.stock
                    orderItem.save()

def check_cart(request):
    order = get_order(request)
    if order:
        for orderItem in get_order(request).orderItems.all():
            if not orderItem.is_valid():
                orderItem.quantity = 0
                orderItem.save()
