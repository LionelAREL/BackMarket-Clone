from django.contrib import admin
from .models import Cart, Order, OrderItem, Adress

admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Adress)
