from django import template

from User.models import reply

register = template.Library()

@register.filter(name='get_val')
def get_val(list,key):
    if reply.objects.filter(user_id=key).exists():
        val = reply.objects.all().filter(user_id=key)
        return val
    else:
        return None