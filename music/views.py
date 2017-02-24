from django.http import HttpResponse
from django.shortcuts import render

import datetime
from .models import Album


def index(request):
    all_album = Album.objects.all()
    return render(request, 'music/index.html', {'all_album': all_album})


def details(request):
    return render(request, 'music/details.html')


def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {0}.</body></html>".format(now)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise HTTP404()
    offset_date = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It is now {0}.</body></html>".format(offset_date)
    return HttpResponse(html)
