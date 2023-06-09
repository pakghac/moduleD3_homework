from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value, arg):
    replaced_words = ['A6MF1', 'NG', 'Hyundai']
    for word in replaced_words:
        value = value.replace(word, arg)
    return value