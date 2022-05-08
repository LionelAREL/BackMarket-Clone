from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('',views.cart,name = "cart"),
    path('shipping/', views.shipping, name='shipping'),
    path('shipping/selectAdress/<int:adressId>', views.selectAdress, name='selectAdress'),
    path('shipping/recap/', views.recap, name='recap'),
]
    
    