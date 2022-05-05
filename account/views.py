from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.urls import reverse

class UserFormLogin(AuthenticationForm):
    fields = ['username','password']

class UserFormSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signUp(request):
    if request.method == 'POST' :
        userForm = UserFormSignUp(data = request.POST)
        if userForm.is_valid():
            userForm.save()
            return HttpResponseRedirect('/')
    else:
        userForm = UserFormSignUp()
    return render(request, 'pages/sign-up.html',{'userForm': userForm}) 

def login(request):
    if request.method == 'POST' :
        userForm = UserFormLogin(data = request.POST)
        if userForm.is_valid():
            return HttpResponseRedirect('/')
    else:
        userForm = UserFormLogin()
    return render(request, 'pages/login.html',{'userForm': userForm}) 

