from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from account.models import User
from django import forms


class UserFormLogin(AuthenticationForm):
    fields = ['username','password']

class UserFormUpdate(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email']
    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=self.instance.username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

 


class UserFormSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']
