from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from catalogue.views import *

app_name = 'account'

urlpatterns = [
    path('login', views.login,name = 'login'),
    path('sign-up', views.signUp,name = 'signUp'),
]
    
    