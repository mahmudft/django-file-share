from django import template

register = template.Library()

@register.filter
def splitslash(value):
    text = value.split("/")
    return text[1]

@register.filter
def splitdbl(value):
    text = value.split("/")
    return text[3]