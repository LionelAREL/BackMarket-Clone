from django.contrib.sessions.base_session import AbstractBaseSession
from django.db import models
from cart.models import Order


class CustomSession(AbstractBaseSession):
    order = models.ForeignKey(Order,blank = True,null=True,on_delete=models.SET_NULL ,db_index=True)

    @classmethod
    def get_session_store_class(cls):
        return SessionStore

from .backends.db import SessionStore