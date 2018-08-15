from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe


register = template.Library()

from ..models import Hostel

@register.simple_tag
def total_hostels():
    return Hostel.vacanthostel.count()


@register.inclusion_tag('hostel/latest_hostels.html')
def show_latest_hostels(count=8):
    latest_hostels = Hostel.vacanthostel.order_by('-created')[:count]
    return {'latest_hostels': latest_hostels}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
