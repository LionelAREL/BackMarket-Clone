from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import get_object_or_404
from django.db.models import F

from catalogue.models import Product

class Cart(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Order(models.Model):
    ordered = models.BooleanField(default=False)
    date = models.DateField(blank=True,null=True)
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cart.user.username}({self.ordered})"

    @property
    def totalOrder(self):
        total = sum([x.quantity * x.product.price for x in self.orderitem_set])



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}({self.quantity})"

    def save(self, *args, **kwargs):
        if(self.quantity == 0):
            self.delete()
            return
        super().save(*args, **kwargs)

    def is_valid(self):
        if self.quantity <= self.product.stock:
            return True
        return False

    @property
    def totalOrderItem(self):
        return self.quantity*self.product.price







