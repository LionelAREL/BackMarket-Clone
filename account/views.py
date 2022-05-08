from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *


def logOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signUp(request):
    userForm = UserFormSignUp()
    if request.method == 'POST' :
        userForm = UserFormSignUp(data = request.POST)
        if userForm.is_valid():
            login(request,userForm.save())
            return redirect('home')
        else:
            print("erreur sign up")
    return render(request, 'pages/sign-up.html',{'userForm': userForm}) 

def loginView(request):
    userForm = UserFormLogin()
    if request.method == 'POST' :
        userForm = UserFormLogin(data = request.POST)
        if userForm.is_valid():
            print("valid")
            login(request, userForm.user_cache)
            return redirect('/')
        else:
            print("erreur login")
    return render(request, 'pages/login.html',{'userForm': userForm})

@login_required(login_url='/account/login')
def accountView(request):
    user = request.user
    return render(request, 'pages/account.html',context={'user':user})


