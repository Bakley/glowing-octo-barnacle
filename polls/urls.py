from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/343/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/343/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/343/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
