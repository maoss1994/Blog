from django.db import models
from blog.models import Post


class Comment(models.Model):
    """文章评论模型"""
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return self.content[:20]


