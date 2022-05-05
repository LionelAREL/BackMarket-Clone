from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('', views.shop,name = 'shop'),
    path('<int:pk>/',views.ProductView.as_view(), name='productDetail'),
    path('<int:pk>/add-to-cart',views.addToCart,name='addToCart'),
    path('<int:pk>/delete-to-cart/<int:orderId>',views.deleteToCart,name='deleteToCart'),
]
    
    