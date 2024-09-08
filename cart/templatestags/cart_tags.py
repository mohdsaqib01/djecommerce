from django import template
# create a object of liberary class
register = template.Library()


@register.filter(context=True)
def cart_item_count(context):
    request
