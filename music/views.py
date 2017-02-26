from django.http import HttpResponse, Http404
from django.shortcuts import render

import datetime
from .models import Album


def index(request):
    all_album = Album.objects.all()
    now = datetime.datetime.now()
    context = {
        'time': now,
        'all_album': all_album

    }
    return render(request, 'music/index.html', context)


def details(request):
    return render(request, 'music/details.html')


# def current_time(request):
#     now = datetime.datetime.now()
#     context = {
#         'time': now,
#     }
#
#     return render(request, 'music/index.html', context)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    offset_date = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It is now {0}.</body></html>".format(offset_date)
    return HttpResponse(html)
