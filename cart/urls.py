from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('',views.Cart.as_view(),name = "cart"),
    path('shipping/', views.Shipping.as_view(), name='shipping'),
    path('shipping/selectAdress/<slug:adressId>', views.SelectAdress.as_view(), name='selectAdress'),
    path('shipping/payment/', views.Payment.as_view(), name='payment'),
    path('shipping/payment/success/', TemplateView.as_view(template_name='pages/success.html'), name='success'),
    path('shipping/payment/cancel/', TemplateView.as_view(template_name='pages/cancel.html'), name='cancel'),
    path('shipping/payment/webHook/',views.WebHook.as_view(),name='webHook')
]
