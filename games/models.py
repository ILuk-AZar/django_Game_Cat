from django.db import models



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    def __str__(self):
        return self.title