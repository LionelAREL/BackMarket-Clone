from django import forms
from cart.models import Adress


class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = '__all__'
        exclude = ['user']