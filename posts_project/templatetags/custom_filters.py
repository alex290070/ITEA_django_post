import random
from django import template

register = template.Library()

@register.filter
def custom_cut(value, arg):
    return value.replace(arg, '')


@register.filter
def shuffle(value):
    return random.shuffle(value)


@register.filter
def phone_format(value):
    return f'+{value[:2]} ({value[2:5]}) {value[5:8]} {value[8:10]} {value[10:]}'
