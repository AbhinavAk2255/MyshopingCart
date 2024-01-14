from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data,size):
    chunk = []
    i=0
    for data in list_data:
        chunk.append(data)
        i = i+1
        if(i == size):
            yield chunk
            chunk = []
            i=0
    yield chunk    