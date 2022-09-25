from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('', views.Shop.as_view(),name = 'shop'),
    path('update-header', views.update_cart,name='updateHeader'),
    path('<int:pk>/',views.ProductView.as_view(), name='productDetail'),
    path('add-to-cart/<slug:productId>/',views.AddToCart.as_view(),name='addToCart'),
    path('delete-to-cart/<slug:orderItemId>/',views.DeleteToCart.as_view(),name='deleteToCart'),
    path('remove/<int:orderItemId>/',views.Remove.as_view(),name='remove'),
    path('buy/<int:orderItemId>/',views.BuyOrder.as_view(),name='buyOrder'),
    path('buy-all/',views.BuyAll.as_view(),name='buyAll'),
]
    
    