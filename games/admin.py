from django.contrib import admin
from .models import Game, Genre

admin.site.register(Genre)
admin.site.register(Game)