from django import template
from django.template.loader import get_template
from core.models import Contact

register = template.Library()


@register.simple_tag
def get_contact():
    return Contact.objects.first()

@register.inclusion_tag('components/footer.html')
def footer():
    context = dict()
    contact = Contact.objects.first()
    if contact:
        context['address'] = contact.address
        context['phone'] = contact.phone
    return context
