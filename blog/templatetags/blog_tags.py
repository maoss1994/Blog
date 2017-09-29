from django import template
from ..models import Post, Category


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-publish')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.all()