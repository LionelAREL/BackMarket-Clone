from django.contrib.auth import get_user_model
from django.db import models
from catalogue.models import Product

class Cart(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

    @property
    def total(self):
        orders = self.order_set
        if orders:
            order = orders.all()[0]
            return order.totalOrder
        return 0

class Adress(models.Model):
    city = models.CharField(max_length=100)
    postCode = models.IntegerField(blank=True)
    adress = models.CharField(max_length=500)
    adressComplement = models.CharField(max_length=500)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.city} ({self.postCode})"


class Order(models.Model):
    ordered = models.BooleanField(default=False)
    date = models.DateField(blank=True,null=True)
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE)
    adress = models.ForeignKey(Adress,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.cart.user.username}({self.ordered})"

    @property
    def totalOrder(self):
        total = sum([x.quantity * x.product.price for x in self.orderitem_set.all()])
        return total

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








