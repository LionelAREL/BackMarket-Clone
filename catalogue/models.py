from django.db import models


class Product(models.Model):
    stock = models.IntegerField(default=1)
    img = models.ImageField(blank = True,null = True, upload_to='img')
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name}:{self.price}({self.stock})"

