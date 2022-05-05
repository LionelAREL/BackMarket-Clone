from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from catalogue.views import *

app_name = "catalogue"

urlpatterns = [
    path('', views.shop,name = 'shop'),
]
    
    