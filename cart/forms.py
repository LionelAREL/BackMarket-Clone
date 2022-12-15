from django import forms
from cart.models import Adress


class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = '__all__'
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget = forms.TextInput(attrs={'placeholder': 'City'})
        self.fields['city'].label = False
        self.fields['zip_code'].widget = forms.TextInput(attrs={'placeholder':'Zip Code'}) 
        self.fields['zip_code'].label = False
        self.fields['address_line_1'].widget = forms.TextInput(attrs={'placeholder':'Adresse line'}) 
        self.fields['address_line_1'].label = False
        self.fields['address_line_2'].widget = forms.TextInput(attrs={'placeholder':'Adresse line complementary'}) 
        self.fields['address_line_2'].label = False