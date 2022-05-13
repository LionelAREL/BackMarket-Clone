from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(),name = 'login'),
    path('sign-up', views.SignUpView.as_view(),name = 'signUp'),
    path('logOut', views.LogOut.as_view(),name = 'logOut'),
    path('account', views.AccountView.as_view(),name = 'account'),
]
