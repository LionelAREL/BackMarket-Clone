from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import FormView, TemplateView, RedirectView, UpdateView
from cart.models import Order
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from account.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

@method_decorator(login_required, name='dispatch')
class Logout(RedirectView):
    permanent = True
    pattern_name = 'home'
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        messages.success(self.request,"You are now logout")
        return super().get_redirect_url(*args, **kwargs)

class SignUpView(FormView):
    form_class = UserFormSignUp
    template_name = 'pages/sign-up.html'
    success_url = '/'

    def form_valid(self, form):
        form = login(request=self.request, user=form.save(commit=True))
        messages.success(self.request,"You're account was successfully created and you are login !!!")
        return super().form_valid(form)

@login_required
def UpdateUserView(request):
    if request.method == 'POST':
        form = UserFormUpdate(request.POST, instance=request.user)
        if form.is_valid():
            user_form = form.save()
            messages.success(self.request,"Your information has been updated")
            return redirect('account:account')
        else:
            return render(request, 'pages/updateUser.html',{'form':form})
    else:
        form = UserFormUpdate(instance=request.user)
        return render(request, 'pages/updateUser.html',{'form':form})

# class LoginView(FormView):
#     template_name = 'pages/login.html'
#     success_url = "/"
#     def form_valid(self, form):
#         login(request=self.request,user=form.user)
#         messages.success(self.request,"Hello, you are now login, happy to see you !")
#         return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    template_name = 'pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['previousOrder'] = Order.objects.filter(user=user,ordered=True)
        return context




