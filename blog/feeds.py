from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    title = "Cluas's Blog Posts"
    link = '/'
    description = "Cluas's Blog Post"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}]{}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body