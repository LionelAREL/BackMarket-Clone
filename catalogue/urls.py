from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('', views.shop,name = 'shop'),
    path('<int:pk>/',views.ProductView.as_view(), name='productDetail'),
    path('add-to-cart/<int:productId>/',views.addToCart,name='addToCart'),
    path('delete-to-cart/<int:orderItemId>/',views.deleteToCart,name='deleteToCart'),
    path('remove/<int:orderItemId>/',views.remove,name='remove'),
    path('buy/<int:orderItemId>/',views.buyOrder,name='buyOrder'),
    path('buy-all/',views.buyAll,name='buyAll'),
]
    
    