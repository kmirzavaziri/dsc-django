from django import template

from main import dictionary
from main.settings import LANGUAGE_CODE

register = template.Library()


@register.simple_tag
def exp(key):
    return dictionary.exp(key)


@register.simple_tag(takes_context=True)
def main_extra_context(context):
    context['language_code'] = LANGUAGE_CODE
    return ''
