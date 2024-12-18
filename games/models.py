from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.ForeignKey(Developer, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    platforms = models.ManyToManyField(Platform)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    def __str__(self):
        return self.title