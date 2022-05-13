from django import forms

from catalogue.models import Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']
        #widgets = {'name':}