from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

# settings value
@register.simple_tag
def setting(name: str) -> str:
    return mark_safe(getattr(settings, name, ""))
