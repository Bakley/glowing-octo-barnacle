from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post = Post.published.all()
    context = {'post': post}
    return render(request,
                  'blog/post/list.html',
                  context)


def post_details(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post': post}
    return render(request, 'blog/post/details.html', context)