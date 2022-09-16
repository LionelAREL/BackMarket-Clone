from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'djangoEcommerce'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(),name = 'home'),
    path('home', views.Home.as_view(),name = 'home'),
    path('shop/',include('catalogue.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)