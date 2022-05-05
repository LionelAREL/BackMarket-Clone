from .models import Product
from django.dispatch import receiver
from django.db.models.signals import *


@receiver(post_delete, sender=Product)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.img.delete(save=False)
    except:
        pass


@receiver(pre_save, sender=Product)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = sender.objects.get(id=instance.id).img.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
