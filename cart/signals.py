from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from cart.utils import merge_cart


@receiver(user_logged_in)
def merge_cart_signal(sender, **kwargs):
    merge_cart(kwargs['request'])