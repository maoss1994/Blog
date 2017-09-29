from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
from comments.forms import CommentForm


def post_detail(request, year, month, day, id):
    post = get_object_or_404(Post,
                             id=id,
                             status='发布',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comments = post.comments.all()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'form': form,
                   'comments': comments})


def index(request):
    posts = Post.published.all()
    return render(request, 'blog/post/index.html', {'posts': posts})


def archives(request, year, month):
    posts = Post.objects.filter(created__year=year,
                                created__month=month)
    return render(request, 'blog/post/index.html', {'posts': posts})


def category(request, name):
    posts = Post.objects.filter(category__name=name)
    return render(request, 'blog/post/index.html', {'posts': posts})