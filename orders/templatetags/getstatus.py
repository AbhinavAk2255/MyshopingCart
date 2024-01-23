from django import template

register = template.Library()

@register.simple_tag(name='getstatus')
def getstatus(status):
    status_list = ['CART_STAGE','CONFIRMED','PROCESSED','DELIVERED','REJECTED']
    return status_list[status]
