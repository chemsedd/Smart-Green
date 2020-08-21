from django import template


register = template.Library()


@register.filter
def concat(arg1, arg2):
    ''' String concatenation: arg1 & arg2 '''
    return f'{arg1}{arg2}'
