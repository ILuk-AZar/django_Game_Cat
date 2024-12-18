from django.apps import AppConfig

class GamesConfig(AppConfig):
    name = 'games'

    def ready(self):
        import games.signals  # Подключаем сигналы

class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'games'
