from django.shortcuts import render
from .models import Album


def index(request):
    all_album = Album.objects.all()
    return render(request, 'music/index.html', {'all_album': all_album})
