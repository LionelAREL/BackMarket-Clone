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

@method_decorator(login_required, name='dispatch')
class LogOut(RedirectView):
    permanent = True
    pattern_name = 'home'
    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)

class SignUpView(FormView):
    form_class = UserFormSignUp
    template_name = 'pages/sign-up.html'
    success_url = '/'

    def form_valid(self, form):
        login(request=self.request, user=form.save(commit=True))
        return super().form_valid(form)

@login_required
def UpdateUserView(request):
    if request.method == 'POST':
        form = UserFormUpdate(request.POST, instance=request.user)
        if form.is_valid():
            user_form = form.save()
            return redirect('account:account')
        else:
            return render(request, 'pages/updateUser.html',{'form':form})
    else:
        form = UserFormUpdate(instance=request.user)
        return render(request, 'pages/updateUser.html',{'form':form})

class LoginView(FormView):
    form_class = UserFormLogin
    template_name = 'pages/login.html'
    success_url = "/"
    def form_valid(self, form):
        login(request=self.request,user=form.user_cache)
        return super().form_valid(form)
    # def post(self,request,*args,**kwargs):
    #     form = self.get_form()
    #     form['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
    #     form['username'].label = False
    #     form['password'].widget = forms.PasswordInput(attrs={'placeholder':'Password'}) 
    #     form['password'].label = False
    #     return super().post(self,request,*args,**kwargs)


@method_decorator(login_required, name='dispatch')
class AccountView(TemplateView):
    template_name = 'pages/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['previousOrder'] = Order.objects.filter(user=user,ordered=True)
        return context




