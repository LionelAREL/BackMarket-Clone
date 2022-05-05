from django.contrib.auth import get_user_model
from django.db import models
from catalogue.models import Product

class Cart(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    date = models.DateField(blank=True,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product.name}:{self.cart.user.username}({self.quantity})"

