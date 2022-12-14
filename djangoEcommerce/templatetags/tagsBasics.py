from django import template

register = template.Library()

def price(value):
    return str(value)[:-2] + "." + str(value)[-2:] + "€"

register.filter('price', price)