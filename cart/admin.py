from django.contrib import admin
from .models import Order, OrderItem, Adress

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Adress)
