from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm,PasswordChangeForm
from account.models import User
from django import forms


class UserFormLogin(AuthenticationForm):
    fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].label = False
        self.fields['password'].widget.attrs['placeholder']='Password'
        self.fields['password'].label = False

class PasswordFormUpdate(PasswordChangeForm):
    fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder']='Old password'
        self.fields['old_password'].label = False
        self.fields['new_password1'].widget.attrs['placeholder']='New password'
        self.fields['new_password1'].label = False
        self.fields['new_password2'].widget.attrs['placeholder']='New password again'
        self.fields['new_password2'].label = False

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].label = False
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['email'].label = False

 


class UserFormSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        print("################")
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['username'].label = False
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['email'].label = False
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label = False
        self.fields['password2'].widget.attrs['placeholder']='Password again'
        self.fields['password2'].label = False
