from django.db import models


# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    poster_url = models.CharField(max_length=2083)
    grade = models.CharField(max_length=20)
    url = models.CharField(max_length=2083)
