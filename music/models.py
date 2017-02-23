from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    full_name = models.ForeignKey(Musician, on_delete=models.CASCADE)
    artist_name = models.CharField(max_length=50)
    album_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    released_date = models.DateField()
    album_logo = models.CharField(max_length=50)

    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    audio_file = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
