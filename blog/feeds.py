from django.contrib.syndication.views import Feed
from .models import Post
from django.template.defaultfilters import truncatechars


class LatestPostsRssFeed(Feed):
    title = "Cluas's Blog "
    link = '/'
    description = "Cluas's Blog"

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return '[{}]{}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body
