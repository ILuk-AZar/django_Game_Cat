from django.contrib import admin
from .models import Game, Genre, Developer, Publisher, Platform

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'publisher', 'release_year', 'price', 'genre')
    list_filter = ('genre', 'developer', 'publisher', 'platforms')
    search_fields = ('title', 'developer__name', 'publisher__name', 'genre__name')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Game, GameAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Platform, PlatformAdmin)