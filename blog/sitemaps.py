from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """文章站点地图"""
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.publish
