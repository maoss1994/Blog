from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/$',
        views.post_detail, name='post_detail'),
    url(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.archives, name='archives'),
    url(r'^category/(?P<name>.+)/$', views.category, name='category'),
    url(r'^$', views.index, name='index'),
]
