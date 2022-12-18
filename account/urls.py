from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from django.urls import reverse_lazy
from .forms import PasswordFormUpdate, UserFormLogin, PasswordSetForm

app_name = 'account'

urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name="pages/login.html",form_class=UserFormLogin,redirect_authenticated_user=True,success_url = reverse_lazy("account:account")),name = 'login'),
    path('sign-up/', views.SignUpView.as_view(),name = 'signUp'),
    path('logout/', views.Logout.as_view(),name = 'logout'),
    path('account/', views.AccountView.as_view(),name = 'account'),
    path('update-user/', views.UpdateUserView,name="updateUser"),
    path("password_reset/", authViews.PasswordResetView.as_view(template_name="pages/passwordReset.html",email_template_name="pages/emailSend.html", success_url = reverse_lazy("account:password_reset_done")), name="password_reset"),
    path("password_reset/done/",authViews.PasswordResetDoneView.as_view(template_name="pages/passwordSent.html"),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",authViews.PasswordResetConfirmView.as_view(template_name="pages/passwordForm.html",success_url = reverse_lazy("account:password_reset_complete"),form_class=PasswordSetForm) ,name="password_reset_confirm"),
    path("reset/done/",authViews.PasswordResetCompleteView.as_view(template_name="pages/passwordDone.html"),name="password_reset_complete"),
    path("password_change/", authViews.PasswordChangeView.as_view(template_name="pages/passwordChange.html",form_class=PasswordFormUpdate,success_url = reverse_lazy("account:password_change_done")), name="password_change"),
    path("password_change/done/",authViews.PasswordChangeDoneView.as_view(template_name="pages/passwordChangeDone.html"),name="password_change_done"),
]
