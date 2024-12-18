from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'developer', 'publisher', 'release_year', 'price', 'genre']