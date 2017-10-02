from django.apps import AppConfig
import algoliasearch_django as algoliaserach
from .index import PostIndex


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        Post = self.get_model('post')
        algoliaserach.register(Post, PostIndex)
