from django.conf.urls import url

from . import views

app_name = "music"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/$', views.details, name='details'),

    # url(r'^/$', views.current_time, name='current_time'),

    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),

]
