from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_details,
        name='post_details'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
