from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def product(self):
        return self.product_set.all()


class Product(models.Model):
    stock = models.IntegerField(default=1)
    img = models.ImageField(blank = True,null = True, upload_to='img')
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    price = models.IntegerField(default=0)
    categorie = models.ManyToManyField(Categorie,blank=True)

    def __str__(self):
        return f"{self.name}:{self.price}({self.stock})"

    @property
    def price_float(self):
        return "{:.2f}".format(self.price / 100)


