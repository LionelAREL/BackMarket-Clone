from catalogue.models import Categorie


def products_choices():
    all = Categorie.objects.all()
    all_choices = [(x.name, x.name) for x in all]
    all_choices.append(('tous', 'tous'))
    return all_choices