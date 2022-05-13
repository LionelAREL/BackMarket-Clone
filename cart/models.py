from django.contrib.auth import get_user_model
from django.db import models
from account.models import User
from catalogue.models import Product


class Adress(models.Model):
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField(blank=True)
    address_line_1 = models.CharField(max_length=500)
    address_line_2 = models.CharField(max_length=500)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=True,null=True,related_name='adresses')

    def __str__(self):
        return f"{self.city} ({self.zip_code})"


class Order(models.Model):
    ordered = models.BooleanField(default=False)
    date = models.DateField(blank=True,null=True)
    user= models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='order')
    adress = models.ForeignKey(Adress,on_delete=models.CASCADE,blank=True,null=True,related_name='adresses')
    payment_id = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"{self.user.username}({self.ordered})"

    @property
    def total_order(self):
        total = sum([x.total_orderItem for x in self.orderItems.all()])
        return total

    @property
    def total_order_float(self):
        return "{:.2f}".format(self.total_order / 100)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='orderItems')

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
    def total_orderItem(self):
        return self.quantity*self.product.price

    @property
    def total_orderItem_float(self):
        return "{:.2f}".format(self.total_orderItem/100)








