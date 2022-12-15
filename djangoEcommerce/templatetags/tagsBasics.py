from django import template

register = template.Library()

def price(value):
    return str(value)[:-2] + "." + str(value)[-2:] + "€"

def placeholder(value, token):
    """ Add placeholder attribute, esp. for form inputs and textareas """
    value.field.widget.attrs["placeholder"] = token
    return value

register.filter('price', price)
register.filter('placeholder', placeholder)