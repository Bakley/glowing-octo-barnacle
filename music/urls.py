from django.conf.urls import url

from . import views

app_name = "music"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.details, name='details'),

    url(r'^$', views.time, name='time'),

    url(r'^$', views.hours_ahead, name='hours_ahead'),

]