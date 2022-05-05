from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from catalogue.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'home'),
    path('shop/',include('catalogue.urls')),
    path('account/',include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)