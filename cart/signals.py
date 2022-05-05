from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from account.models import User
from cart.models import Cart


@receiver(post_save, sender=User)
def my_handler(instance,created, **kwargs):
    if created:
        cart = Cart(user = instance)
        cart.save()
