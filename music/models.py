from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    full_name = models.ForeignKey(Musician, on_delete=models.CASCADE)
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    released_date = models.DateField()
    Logo = models.CharField(max_length=50)

    def __str__(self):
        return self.Title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    audio_file = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
