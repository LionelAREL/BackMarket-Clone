from django import forms
from .utils import products_choices


class SearchForm(forms.Form):
    search_text = forms.CharField(label='recherche',max_length=200,required=False)
    categorie = forms.ChoiceField(label='categorie',initial='tous',choices=products_choices())

