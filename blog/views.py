from django.shortcuts import render, get_object_or_404
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginated_by = 3  # 3 posts in each page
    template_name = 'blog/post/list.html'


def post_details(request, year, month, day, post):
    posts = get_object_or_404(Post,
                              slug=post,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    context = {'posts': posts}
    return render(request, 'blog/post/details.html', context)
