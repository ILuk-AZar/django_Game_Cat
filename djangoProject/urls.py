from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
path('', include('games.urls')),
]