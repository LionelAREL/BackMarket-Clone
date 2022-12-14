from django.views.generic import TemplateView
from catalogue.models import Product
import os


class Home(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all().order_by('date')[:8]
        print(products)
        context['latest'] = products
        listCarouselle1= os.listdir('./static/carouselle-1')
        print(listCarouselle1)
        context['carouselle1'] = listCarouselle1
        return context