from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from account.models import User


class UserFormLogin(AuthenticationForm):
    fields = ['username','password']

class UserFormSignUp(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
