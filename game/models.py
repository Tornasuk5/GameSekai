from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=70)
    developer = models.CharField(max_length=50)
    date_release = models.CharField(max_length=10)
    img = models.TextField()
    trailer = models.TextField()
    val = models.FloatField()
