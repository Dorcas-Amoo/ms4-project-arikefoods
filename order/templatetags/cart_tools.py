from django import template

""" The code below was generated from
    Code Institute's Boutique Ado Tutorial """

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
